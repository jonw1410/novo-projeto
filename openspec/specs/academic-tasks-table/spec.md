# academic-tasks-table Specification

## Purpose
Define the database schema, field constraints, relationships, and indexing strategy for managing student academic tasks in EduTrack AI.

## Requirements

### Requirement: Academic Tasks Table Definition
The system SHALL define the `academic_tasks` table in Xano with `auth = false` to store academic tasks and assignments for students.

#### Scenario: Table initialization
- **WHEN** the `academic_tasks` table schema is compiled
- **THEN** the system sets `auth = false`
- **AND** registers the table name as `academic_tasks`.

### Requirement: Academic Tasks Schema Fields
The system SHALL declare the required fields for `academic_tasks`: `id` (int primary key auto-increment), `created_at` (timestamp private), `title` (text trim), `description` (text trim), `due_date` (timestamp/date), `status` (text with default "Pendente"), `subject_id` (foreign key to `subjects`), and `user_id` (foreign key to `usuarios`).

#### Scenario: Creating a valid task record
- **WHEN** a task record is inserted with title, description, due date, status, subject_id, and user_id
- **THEN** the system stores the record
- **AND** validates foreign key relationships against `subjects` and `usuarios`.

### Requirement: Academic Tasks Indexing Strategy
The system SHALL define indexes to optimize querying and ensure tenant isolation: primary index on `id`, btree index on `user_id` (asc), btree index on `subject_id` (asc), and btree index on `created_at` (desc).

#### Scenario: Querying tasks by user and subject
- **WHEN** a query filters tasks by `user_id` and `subject_id`
- **THEN** the database utilizes the btree indexes on `user_id` and `subject_id` for fast index scans.
