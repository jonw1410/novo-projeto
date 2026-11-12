## Context

EduTrack AI currently manages student data across `user`, `subjects`, and `academic_tasks`. To provide a consolidated view of student progress, the system requires a scriptable reporting tool in Python to compile performance metrics into a PDF file and an authenticated backend endpoint in Xano to deliver this report.

## Goals / Non-Goals

**Goals:**
- Provide a Python CLI script `scripts/generate_performance_report.py` that computes academic performance metrics (total courses, completed tasks, pending tasks, completion percentage) and saves a PDF report.
- Create an authenticated endpoint `api/reports/student_performance_GET.xs` in Xano with `auth = "user"` returning the user's performance metrics and downloadable report data.
- Ensure all logic operates offline-ready using the existing pure-Python PDF generator (`utils/pdf_generator.py`).

**Non-Goals:**
- Pushing or deploying changes directly to remote Xano servers (violates AGENTS.md Rule #2).
- Modifying underlying database schemas in `table/*.xs`.

## Decisions

1. **Python Script Architecture:**
   - Place the script in `scripts/generate_performance_report.py`.
   - Support both command-line execution with credentials/token or mock mode for local testing.
   - Use `utils.pdf_generator.build_pdf_document` to build the PDF binary.

2. **Xano Endpoint Architecture:**
   - Group: `reports` under `api/reports/`.
   - Endpoint: `query "reports/student_performance" verb=GET`.
   - Authentication: `auth = "user"`, filtering DB queries strictly with `$auth.id`.
   - Return: Structured JSON containing performance statistics and report metadata.

## Risks / Trade-offs

- **[Unauthenticated Access]** → Enforce `auth = "user"` on the Xano query to prevent unauthorized access.
- **[No External Dependencies]** → Rely solely on the project's native PDF generation capabilities without external libraries.
