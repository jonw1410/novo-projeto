# Change: logica-calculo-progresso

## Why
Students and academic administrators need to track academic progress for each subject in real time. Calculating the percentage of completed tasks relative to total tasks for a given subject provides accurate completion metrics that can be consumed by other modules or external consumers via a structured JSON format.

## What Changes
- Create a Python script in `scripts/calculate_progress.py` that connects to the academic tasks CRUD endpoint (`GET /academic_tasks`).
- Implement progress calculation logic based on tasks associated with a specific discipline (`subject_id`): `progress = (completed_tasks / total_tasks) * 100`.
- Return the calculated progress in structured JSON format containing total tasks, completed tasks, and calculated progress percentage.

## Impact
- **New Scripts**: Adds `scripts/calculate_progress.py`.
- **Backend Schema**: No changes to database tables or Xano backend schemas (reuses existing `academic_tasks` and `subjects`).
- **Dependencies**: Uses `requests` and `python-dotenv` already available in the project environment.
