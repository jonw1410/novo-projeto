"""
EduTrack AI - Academic Progress Calculation Script
Calculates subject completion percentage based on its associated tasks fetched from the CRUD endpoint.
Returns structured JSON metrics.
"""

import argparse
import json
import os
import sys
from typing import Any, Dict, List, Optional, Union
import requests
from dotenv import load_dotenv

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    from utils.xano_client import get_config_value
except ImportError:
    def get_config_value(key: str, default: str = "") -> str:
        return os.getenv(key, default)

# Load environment variables from .env at project root
load_dotenv()

DEFAULT_AUTH_API_URL = "https://x8ki-letl-twmt.n7.xano.io/api:cPkbqL8B"
DEFAULT_TASKS_API_URL = "https://x8ki-letl-twmt.n7.xano.io/api:VIQ0W9tI"
COMPLETED_STATUSES = {"concluida", "concluída", "completed", "done", "finished"}


def normalize_status(status: Optional[str]) -> str:
    """Normalize status string by stripping whitespace and converting to lowercase."""
    if not status:
        return ""
    return str(status).strip().lower()


def authenticate_user(
    email: Optional[str] = None,
    password: Optional[str] = None,
    auth_base_url: Optional[str] = None
) -> Optional[str]:
    """
    Authenticate with Xano auth/login endpoint to retrieve an auth token.
    Reads credentials from arguments or from XANO_USER_EMAIL / XANO_USER_PASSWORD in .env.
    """
    resolved_email = email or get_config_value("XANO_USER_EMAIL")
    resolved_password = password or get_config_value("XANO_USER_PASSWORD")
    resolved_auth_url = (
        auth_base_url
        or get_config_value("XANO_BASE_URL")
        or DEFAULT_AUTH_API_URL
    ).rstrip("/")

    if not resolved_email or not resolved_password:
        return None

    try:
        login_url = f"{resolved_auth_url}/auth/login"
        response = requests.post(
            login_url,
            json={"email": resolved_email.strip().lower(), "password": resolved_password},
            timeout=10
        )
        response.raise_for_status()
        auth_data = response.json()
        token = auth_data.get("authToken") or auth_data.get("token") or auth_data.get("jwt")
        return token
    except requests.RequestException as exc:
        sys.stderr.write(f"Warning: Automatic login attempt failed ({exc}).\n")
        return None


def calculate_subject_progress(tasks: List[Dict[str, Any]], subject_id: int) -> Dict[str, Any]:
    """
    Calculate progress percentage for a given subject based on its tasks.

    Formula: (completed_tasks / total_tasks) * 100
    Returns 0.0% if there are no tasks for the subject.
    """
    try:
        subject_id_int = int(subject_id)
    except (ValueError, TypeError):
        subject_id_int = subject_id

    subject_tasks = [
        task for task in tasks
        if task.get("subject_id") == subject_id_int or str(task.get("subject_id")) == str(subject_id)
    ]

    total_tasks = len(subject_tasks)
    completed_tasks = sum(
        1 for task in subject_tasks
        if normalize_status(task.get("status")) in COMPLETED_STATUSES
    )

    if total_tasks > 0:
        progress_percentage = round((completed_tasks / total_tasks) * 100.0, 2)
    else:
        progress_percentage = 0.0

    return {
        "subject_id": subject_id_int,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": total_tasks - completed_tasks,
        "progress_percentage": progress_percentage
    }


def fetch_academic_tasks(
    base_url: Optional[str] = None,
    auth_token: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None
) -> List[Dict[str, Any]]:
    """
    Fetch academic tasks list from the Xano CRUD endpoint (GET /academic_tasks).
    Requires a valid JWT Bearer token because the endpoint filters tasks by $auth.id.
    """
    resolved_base_url = (
        base_url
        or get_config_value("XANO_TASKS_BASE_URL")
        or DEFAULT_TASKS_API_URL
    ).rstrip("/")

    endpoint = f"{resolved_base_url}/academic_tasks"
    headers: Dict[str, str] = {"Content-Type": "application/json"}

    # Resolve token directly, or attempt automatic authentication
    resolved_token = auth_token or get_config_value("XANO_AUTH_TOKEN")
    if not resolved_token:
        resolved_token = authenticate_user(email=email, password=password)

    if resolved_token:
        headers["Authorization"] = f"Bearer {resolved_token}"
    else:
        sys.stderr.write(
            "Note: No auth token provided. The endpoint GET /academic_tasks requires authentication ($auth.id).\n"
            "Provide --token <token>, configure XANO_AUTH_TOKEN in .env, or provide --email/--password (or XANO_USER_EMAIL / XANO_USER_PASSWORD in .env).\n"
        )

    try:
        response = requests.get(endpoint, headers=headers, timeout=10)
        response.raise_for_status()
        tasks_data = response.json()
        if isinstance(tasks_data, list):
            return tasks_data
        elif isinstance(tasks_data, dict) and "items" in tasks_data:
            return tasks_data["items"]
        return []
    except requests.HTTPError as exc:
        if exc.response is not None and exc.response.status_code == 401:
            sys.stderr.write(
                "Error 401 Unauthorized: The Xano endpoint requires a valid Bearer token from a logged-in user.\n"
            )
        else:
            sys.stderr.write(f"Warning: Failed to fetch tasks from CRUD endpoint ({exc}).\n")
        raise
    except requests.RequestException as exc:
        sys.stderr.write(f"Warning: Network error connecting to CRUD endpoint ({exc}).\n")
        raise


def get_subject_progress(
    subject_id: int,
    tasks: Optional[List[Dict[str, Any]]] = None,
    base_url: Optional[str] = None,
    auth_token: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None,
    as_json: bool = True
) -> Union[str, Dict[str, Any]]:
    """
    Retrieve or compute progress for a specific subject and return JSON or dict.
    """
    if tasks is None:
        try:
            tasks = fetch_academic_tasks(
                base_url=base_url,
                auth_token=auth_token,
                email=email,
                password=password
            )
        except requests.RequestException:
            tasks = []

    progress_data = calculate_subject_progress(tasks=tasks, subject_id=subject_id)

    if as_json:
        return json.dumps(progress_data, indent=2, ensure_ascii=False)
    return progress_data


def main() -> None:
    """CLI execution entrypoint."""
    parser = argparse.ArgumentParser(description="Calculate subject progress from academic tasks CRUD.")
    parser.add_argument("--subject-id", type=int, default=1, help="ID of the subject to calculate progress for (default: 1)")
    parser.add_argument("--token", type=str, default=None, help="Xano auth Bearer token (JWT)")
    parser.add_argument("--email", type=str, default=None, help="User email for automatic login")
    parser.add_argument("--password", type=str, default=None, help="User password for automatic login")
    parser.add_argument("--base-url", type=str, default=None, help="Optional Xano tasks API base URL")
    parser.add_argument("--demo", action="store_true", help="Run with mock task data without needing network/auth")

    args = parser.parse_args()

    if args.demo:
        demo_tasks = [
            {"id": 1, "title": "Setup Dev Environment", "subject_id": args.subject_id, "status": "concluída"},
            {"id": 2, "title": "Read Chapter 1", "subject_id": args.subject_id, "status": "concluída"},
            {"id": 3, "title": "Submit Assignment 1", "subject_id": args.subject_id, "status": "pendente"},
            {"id": 4, "title": "Final Project Review", "subject_id": args.subject_id, "status": "pendente"},
            {"id": 5, "title": "Other Subject Task", "subject_id": 999, "status": "concluída"},
        ]
        result_json = get_subject_progress(subject_id=args.subject_id, tasks=demo_tasks, as_json=True)
    else:
        result_json = get_subject_progress(
            subject_id=args.subject_id,
            base_url=args.base_url,
            auth_token=args.token,
            email=args.email,
            password=args.password,
            as_json=True
        )

    print(result_json)


if __name__ == "__main__":
    main()
