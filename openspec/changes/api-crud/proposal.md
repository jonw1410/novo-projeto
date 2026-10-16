# Change: api-crud

## Why
Currently in EduTrack AI, backend persistence for academic subjects (`subjects`) and tasks (`academic_tasks`) lacks dedicated RESTful CRUD endpoints in Xano. Users need secure, tenant-isolated APIs to create, list, update, and delete their own subjects and tasks, ensuring no cross-user data leakage.

## What Changes
- Create table `academic_tasks` in `tables/academic_tasks.xs` with foreign key relation to `usuarios` and `subjects`.
- Create authenticated CRUD endpoints for `subjects` in `apis/subjects/`:
  - `POST /subjects`: Create a new subject associated with `$auth.id`.
  - `GET /subjects`: List all subjects belonging to `$auth.id`.
  - `PATCH /subjects/{id}`: Update a specific subject owned by `$auth.id`.
  - `DELETE /subjects/{id}`: Delete a specific subject owned by `$auth.id`.
- Create authenticated CRUD endpoints for `academic_tasks` in `apis/academic_tasks/`:
  - `POST /academic_tasks`: Create a new task associated with `$auth.id`.
  - `GET /academic_tasks`: List all tasks belonging to `$auth.id`.
  - `PATCH /academic_tasks/{id}`: Update a specific task owned by `$auth.id`.
  - `DELETE /academic_tasks/{id}`: Delete a specific task owned by `$auth.id`.

## Capabilities

### New Capabilities
- `subjects-api`: Authenticated REST CRUD operations for academic subjects scoped to the logged-in user.
- `academic-tasks-api`: Authenticated REST CRUD operations for academic tasks scoped to the logged-in user.

## Impact
- **Database Tables**: Creates `tables/academic_tasks.xs` and utilizes `tables/subjects.xs`.
- **API Groups**: Creates endpoint files under `apis/subjects/` and `apis/academic_tasks/`.
