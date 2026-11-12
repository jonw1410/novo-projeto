"""
EduTrack AI - Student Performance Report Generation Script
Calculates student academic performance metrics (subjects, tasks, completion rates)
and compiles a clean PDF performance report document.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from typing import Any, Dict, List, Optional
import requests
from dotenv import load_dotenv

# Ensure root directory is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.pdf_generator import build_pdf_document
from utils.xano_client import get_endpoint_urls, request_with_fallback

load_dotenv()

COMPLETED_STATUSES = {"concluida", "concluída", "completed", "done", "finished"}


def is_task_completed(status: Optional[str]) -> bool:
    """Check if a task status corresponds to completed."""
    if not status:
        return False
    return str(status).strip().lower() in COMPLETED_STATUSES


def fetch_student_data(token: str) -> Dict[str, Any]:
    """Fetch subjects and tasks from Xano using authenticated JWT token."""
    urls = get_endpoint_urls()
    headers = {"Authorization": f"Bearer {token}"}

    # Fetch subjects
    sub_resp, _ = request_with_fallback(
        "GET",
        f"{urls['subjects']}/subjects",
        urls["fallback_subjects"],
        headers=headers
    )
    sub_resp.raise_for_status()
    subjects = sub_resp.json() if isinstance(sub_resp.json(), list) else []

    # Fetch tasks
    tasks_resp, _ = request_with_fallback(
        "GET",
        f"{urls['tasks']}/academic_tasks",
        urls["fallback_tasks"],
        headers=headers
    )
    tasks_resp.raise_for_status()
    tasks = tasks_resp.json() if isinstance(tasks_resp.json(), list) else []

    return {"subjects": subjects, "tasks": tasks}


def get_mock_student_data(student_name: str = "Aluno Exemplo") -> Dict[str, Any]:
    """Generate mock data for offline testing and dry runs."""
    return {
        "student_name": student_name,
        "subjects": [
            {"id": 1, "name": "Algoritmos e Estrutura de Dados", "teacher": "Dr. Silva", "hours": 80},
            {"id": 2, "name": "Banco de Dados e SQL", "teacher": "Dra. Santos", "hours": 60},
            {"id": 3, "name": "Engenharia de Software", "teacher": "Prof. Oliveira", "hours": 60},
        ],
        "tasks": [
            {"id": 101, "title": "Implementar Arvore Binaria", "subject_id": 1, "status": "Concluída", "due_date": "2026-03-15"},
            {"id": 102, "title": "Exercicios de Complexidade", "subject_id": 1, "status": "Concluída", "due_date": "2026-03-20"},
            {"id": 103, "title": "Modelagem de Dados ER", "subject_id": 2, "status": "Concluída", "due_date": "2026-03-25"},
            {"id": 104, "title": "Normalizacao 3FN", "subject_id": 2, "status": "Pendente", "due_date": "2026-04-05"},
            {"id": 105, "title": "Diagrama de Casos de Uso", "subject_id": 3, "status": "Pendente", "due_date": "2026-04-10"},
        ]
    }


def compute_performance_metrics(subjects: List[Dict[str, Any]], tasks: List[Dict[str, Any]], student_name: str = "Aluno") -> Dict[str, Any]:
    """Calculate overall and per-subject academic performance indicators."""
    total_subjects = len(subjects)
    total_hours = sum(int(s.get("hours") or 0) for s in subjects)
    
    total_tasks = len(tasks)
    completed_tasks = sum(1 for t in tasks if is_task_completed(t.get("status")))
    pending_tasks = total_tasks - completed_tasks
    completion_rate = round((completed_tasks / total_tasks * 100), 1) if total_tasks > 0 else 0.0

    if completion_rate >= 80.0:
        performance_status = "Excelente"
    elif completion_rate >= 60.0:
        performance_status = "Bom"
    elif completion_rate >= 40.0:
        performance_status = "Regular"
    else:
        performance_status = "Em Atencao"

    # Per-subject breakdown
    subject_details = []
    for s in subjects:
        s_id = s.get("id")
        s_tasks = [t for t in tasks if t.get("subject_id") == s_id]
        s_total = len(s_tasks)
        s_completed = sum(1 for t in s_tasks if is_task_completed(t.get("status")))
        s_pending = s_total - s_completed
        s_rate = round((s_completed / s_total * 100), 1) if s_total > 0 else 0.0

        subject_details.append({
            "id": s_id,
            "name": s.get("name", "Sem Nome"),
            "teacher": s.get("teacher", "N/A"),
            "hours": s.get("hours", 0),
            "total_tasks": s_total,
            "completed_tasks": s_completed,
            "pending_tasks": s_pending,
            "completion_rate": s_rate,
        })

    return {
        "student_name": student_name,
        "generation_date": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "total_subjects": total_subjects,
        "total_hours": total_hours,
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "pending_tasks": pending_tasks,
        "completion_rate": completion_rate,
        "performance_status": performance_status,
        "subject_details": subject_details,
    }


def generate_pdf_report(metrics: Dict[str, Any], output_path: str) -> str:
    """Compile metrics into a PDF document and save to disk."""
    metadata = {
        "Estudante": str(metrics["student_name"]),
        "Total de Disciplinas": f"{metrics['total_subjects']} disciplinas ({metrics['total_hours']} horas)",
        "Tarefas Totais": str(metrics["total_tasks"]),
        "Tarefas Concluidas": f"{metrics['completed_tasks']} ({metrics['completion_rate']}%)",
        "Tarefas Pendentes": str(metrics["pending_tasks"]),
        "Desempenho Geral": str(metrics["performance_status"]),
    }

    sections = []
    
    # Section: Per-Subject Performance
    subject_items = []
    for sub in metrics.get("subject_details", []):
        header = f"{sub['name']} ({sub['hours']}h) - Prof. {sub['teacher']}"
        detail = (
            f"Conclusao: {sub['completion_rate']}% | "
            f"Tarefas Concluidas: {sub['completed_tasks']}/{sub['total_tasks']} | "
            f"Pendentes: {sub['pending_tasks']}"
        )
        subject_items.append({"header": header, "detail": detail})

    sections.append({
        "title": "Desempenho por Disciplina",
        "items": subject_items,
    })

    pdf_bytes = build_pdf_document(
        title="EduTrack AI - Relatorio de Desempenho",
        subtitle=f"Desempenho Academico - {metrics['student_name']}",
        metadata=metadata,
        sections=sections
    )

    # Ensure parent directory exists
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    with open(output_path, "wb") as f:
        f.write(pdf_bytes)

    return os.path.abspath(output_path)


def main():
    parser = argparse.ArgumentParser(description="Gera relatório de desempenho acadêmico em PDF")
    parser.add_argument("--output", "-o", default="relatorio_desempenho.pdf", help="Caminho do arquivo PDF de saída")
    parser.add_argument("--student-name", default="Aluno", help="Nome do aluno")
    parser.add_argument("--token", default=None, help="Token JWT de autenticação Xano")
    parser.add_argument("--mock", action="store_true", help="Utilizar dados simulados para teste offline")
    args = parser.parse_args()

    token = args.token or os.getenv("XANO_AUTH_TOKEN")
    student_name = args.student_name

    if token and not args.mock:
        try:
            print(f"[*] Consultando dados acadêmicos no Xano com token...")
            data = fetch_student_data(token)
            subjects = data.get("subjects", [])
            tasks = data.get("tasks", [])
        except Exception as exc:
            print(f"[!] Erro ao conectar ao Xano: {exc}. Utilizando dados simulados de teste...", file=sys.stderr)
            mock = get_mock_student_data(student_name)
            subjects = mock["subjects"]
            tasks = mock["tasks"]
    else:
        print("[*] Modo de simulação/offline ativo. Gerando relatório com métricas acadêmicas de teste...")
        mock = get_mock_student_data(student_name)
        subjects = mock["subjects"]
        tasks = mock["tasks"]

    metrics = compute_performance_metrics(subjects, tasks, student_name=student_name)
    saved_path = generate_pdf_report(metrics, args.output)

    result = {
        "status": "success",
        "output_file": saved_path,
        "file_size_bytes": os.path.getsize(saved_path),
        "metrics": metrics,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
