# Change: Define 'subjects' Table Schema in Xano (schema-subjects-table)

## Why
Currently in the Xano backend (`x8ki-letl-twmt.xano.io`, Workspace 156517), only the `usuarios` (auth) and `user_otp` tables exist. To support multi-tenant academic tracking in EduTrack AI, subjects (disciplinas) must be persisted in a dedicated database table linked to the authenticated user.

Per `AGENTS.md`, orchestrating table creation requires defining field types, foreign key relationships, indexes, and sequencing (creating the table structure before linking cross-references) so that the specialized **Xano Table Designer** can execute the XanoScript implementation reliably.

## What Changes
- Define the formal schema for the `subjects` table in XanoScript syntax.
- **Fields**:
  - `id`: Integer auto-increment (Primary Key).
  - `created_at`: Timestamp with default value `now` and private visibility.
  - `name`: Text with `filters=trim` (Subject title).
  - `teacher`: Text with `filters=trim` (Professor / Instructor name).
  - `hours`: Integer (Total academic hours / workload).
  - `user_id`: Integer Foreign Key referencing `usuarios.id` (`table = "usuarios"`).
- **Index Strategy**:
  - Primary key index on `id`.
  - B-tree index on `user_id` (asc) for efficient user-isolated queries.
  - B-tree index on `created_at` (desc) for sorting by creation date.
- **Agent Orchestration**:
  - Provide complete blueprint adhering to `AGENTS.md` guidelines.
  - Specify handoff instructions for **Xano Table Designer** to create `tables/subjects.xs` and push changes to Xano via `#tool:xano.xanoscript/push_all_changes_to_xano`.

## Impact
- **Specs**: `specs/subjects-table/spec.md`
- **Affected code/files**: `tables/subjects.xs` (new), `tables/800568_usuarios.xs` (target relationship)
