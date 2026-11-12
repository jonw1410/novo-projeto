## Why

Students and academic advisors in EduTrack AI need a consolidated, exportable overview of individual student academic performance, including enrolled subjects, completion rates of academic tasks, workload statistics, and overall progress. Providing an automated Python script to generate a structured student performance PDF along with a dedicated Xano endpoint ensures secure generation, storage, and retrieval of these reports.

## What Changes

- Create a specialized Python reporting script (`scripts/generate_performance_report.py`) that computes student performance metrics (tasks completed vs pending, subject progress, hours) and compiles a formatted PDF report.
- Create an authenticated endpoint in Xano (`GET /reports/student_performance` or `POST /reports/student_performance`) allowing the client to request and download the generated performance document.
- Support storing or delivering the PDF payload securely linked to the authenticated user's ID (`$auth.id`).

## Capabilities

### New Capabilities
- `student-performance-report`: Generates and serves a comprehensive student performance PDF report detailing course progress, task completion metrics, and academic statistics, accessible via Python script and downloadable through a dedicated authenticated Xano endpoint.

## Impact

- **New Scripts**: Adds `scripts/generate_performance_report.py` for headless and automated PDF compilation.
- **Backend Endpoints**: Adds report download query in `api/reports/` (e.g. `api/reports/student_performance_GET.xs`) requiring user authentication (`auth = "user"`).
- **Client Integrations**: Enables Streamlit frontend and external consumers to trigger and download student performance records.
