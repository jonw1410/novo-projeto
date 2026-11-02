# Technical Design: logica-calculo-progresso

## Context
EduTrack AI manages subjects and academic tasks using Xano backend endpoints. Users need to measure progress across subjects based on completed tasks. A standalone script `scripts/calculate_progress.py` is needed to perform this computation by querying tasks from the existing CRUD endpoint and producing structured JSON metrics.

## Goals / Non‑Goals

**Goals:**
- Implement `scripts/calculate_progress.py` in Python.
- Fetch task data using the CRUD endpoint `GET /academic_tasks` using the base URL and auth token.
- Calculate subject progress as `(completed_tasks / total_tasks) * 100`.
- Output the calculation result in JSON format.

**Non‑Goals (Strict Scope Enforcement per AGENTS.md):**
- No database table creations or modifications in Xano.
- No new Xano API endpoints or functions.
- No push/sync/deploy commands to Xano.
- No modifications to Streamlit UI pages in this change.

## Decisions

### 1. Script Architecture (`scripts/calculate_progress.py`)
- Define reusable function `calculate_subject_progress(tasks: list, subject_id: int) -> dict`:
  - Filters tasks where `task.get("subject_id") == subject_id`.
  - Considers completed tasks where status normalized is `"concluída"`, `"concluida"`, or `"completed"`.
  - Calculates percentage: `round((completed / total) * 100.0, 2)` if total > 0 else `0.0`.
  - Returns dictionary with `{ "subject_id": subject_id, "total_tasks": total, "completed_tasks": completed, "progress_percentage": percentage }`.
- Provide `fetch_tasks(api_base_url: str, auth_token: str) -> list` to query `GET /academic_tasks`.
- CLI execution block (`if __name__ == "__main__":`) that accepts arguments or loads environment configuration via `.env`, computes the progress, and prints `json.dumps(result, indent=2)`.

### 2. Error Handling & Resilience
- Division by zero handled safely (0 total tasks returns 0.0%).
- Graceful error messaging if API call fails or `.env` credentials are missing.

## Risks / Trade‑offs
- **Status casing**: Different tasks might use "Concluída", "concluida", or "completed". The function normalizes string case and accents to ensure accurate counts.
- **Network availability**: The calculation function can operate both on raw task lists in memory and via HTTP request to Xano.
