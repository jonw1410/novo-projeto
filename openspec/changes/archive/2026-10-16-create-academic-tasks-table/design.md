# Technical Design: create-academic-tasks-table

## Context
See `proposal.md` for background and motivation. This design specifies the database schema, field options, relationships, and indexing structure for the `academic_tasks` table in EduTrack AI, adhering to XanoScript syntax and EduTrack AI architecture guidelines.

## Goals / Non-Goals

**Goals:**
- Define the relational schema for `academic_tasks` in XanoScript (`table/academic_tasks.xs`).
- Include all fields requested by user: `title` (text), `description` (text), `due_date` (date/timestamp), `status` (text), and `subject_id` (foreign key to `subjects`).
- Include architectural fields required by EduTrack AI: `id` (int primary key), `created_at` (private timestamp), and `user_id` (foreign key to `usuarios` ensuring multi-tenant data isolation).
- Configure indexes to support filtering by user and subject.

**Non-Goals (Strict Scope Enforcement per AGENTS.md):**
- DO NOT create API endpoints (e.g. GET, POST, PATCH, DELETE /academic_tasks) as they were not requested in this change.
- DO NOT create frontend components or modify Streamlit UI.
- DO NOT create automated test suites.
- DO NOT attempt automated push/sync/deploy to Xano Cloud (manual push is developer responsibility).

## Decisions

### 1. Data Model (`table/academic_tasks.xs`)
- **Table Name**: `academic_tasks`
- **Auth Setting**: `auth = false` (standard relational table, not auth table)
- **Fields**:
  - `id`: `int` (Auto-increment Primary Key)
  - `created_at`: `timestamp?=now { visibility = "private" }`
  - `title`: `text filters=trim` (Task title, required)
  - `description`: `text? filters=trim` (Optional task details or notes)
  - `due_date`: `timestamp?` (Task due date / deadline)
  - `status`: `text?="Pendente" filters=trim` (Default status set to "Pendente")
  - `subject_id`: `int { table = "subjects" }` (Foreign key to `subjects` table)
  - `user_id`: `int { table = "usuarios" }` (Foreign key to `usuarios` table for multi-tenancy)
- **Indexes**:
  - Primary index on `id`
  - B-tree index on `user_id` (asc) for tenant isolation
  - B-tree index on `subject_id` (asc) for filtering tasks by subject
  - B-tree index on `created_at` (desc) for chronological ordering

### 2. Architecture & File Location
- File will be placed in `table/academic_tasks.xs` (the repository standard directory for Xano table definitions).

## Risks / Trade-offs
- **Foreign Key Integrity**: In Xano, `subject_id` references `subjects` and `user_id` references `usuarios`. If a referenced subject or user is deleted, orphaned tasks could result unless handled at application layer or cascade policy.
- **Tenant Isolation**: When APIs are planned in subsequent changes, queries must filter by both `id` and `$auth.id` (`user_id`).
