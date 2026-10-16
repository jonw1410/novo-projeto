# Change: create-academic-tasks-table

## Why
Students in EduTrack AI need to track and manage their academic commitments—such as assignments, exams, homework, and projects—linked directly to their registered subjects. Defining a dedicated relational schema for `academic_tasks` in Xano enables structured persistence and multi-tenant isolation per student.

## What Changes
- Define and plan the database schema for the `academic_tasks` table in XanoScript (`table/academic_tasks.xs`).
- Specify table fields:
  - `id`: Auto-increment integer primary key.
  - `created_at`: Private timestamp defaulting to current time.
  - `title`: Text field for the assignment or task title with trim filter.
  - `description`: Text field for task details and notes with trim filter.
  - `due_date`: Date/timestamp field for deadline tracking.
  - `status`: Text field with default value "Pendente".
  - `subject_id`: Foreign key reference to the `subjects` table.
  - `user_id`: Foreign key reference to the `usuarios` table (guaranteeing student tenant isolation per EduTrack AI rules).
- Configure table indexes for primary key, user lookup, subject filtering, and chronological sorting.

## Capabilities

### New Capabilities
- `academic-tasks-table`: Relational schema definition and indexing strategy for academic tasks in Xano Cloud.

## Impact
- **Database Tables**: Creates/updates `table/academic_tasks.xs` (and mirror in `tables/academic_tasks.xs`).
- **Dependencies**: References `table/subjects.xs` and `table/usuarios.xs`.
