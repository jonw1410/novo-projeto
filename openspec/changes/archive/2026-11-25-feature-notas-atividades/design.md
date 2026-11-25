# Technical Design: feature-notas-atividades

## Context
See `proposal.md` for background and motivation. This design details the schema and REST endpoint needed to enable professors to assign grades to students for specific activities in Xano.

## Goals / Non-Goals

**Goals:**
- Design relational schema for table `activity_grades` in XanoScript.
- Design `POST /activity_grades` endpoint to accept and validate grade submissions.

**Non-Goals (Strict Scope Enforcement per AGENTS.md):**
- DO NOT create GET endpoints (e.g. `GET /academic_tasks/{id}/grades`, `GET /users/{id}/grades`) as these were not requested.
- DO NOT create frontend components or modify Streamlit UI.
- DO NOT create automated test suites.
- DO NOT attempt automated push/sync to Xano Cloud (manual push is developer responsibility).

## Decisions

### 1. Data Model (`tables/activity_grades.xs`)
- **Table Name**: `activity_grades`
- **Fields**:
  - `id`: `int` (Auto-increment Primary Key)
  - `created_at`: `timestamp?=now` (`visibility = "private"`)
  - `activity_id`: `int` (Identifier of the activity/task being evaluated)
  - `student_id`: `int { table = "usuarios" }` (Foreign key to student user)
  - `professor_id`: `int { table = "usuarios" }` (Foreign key to instructor user)
  - `grade`: `decimal` (Numerical evaluation from 0.0 to 10.0)
  - `feedback`: `text?` (Optional comments or formative feedback)
- **Indexes**:
  - Primary index on `id`
  - B-tree index on `student_id` (asc)
  - B-tree index on `activity_id` (asc)

### 2. API Endpoint (`apis/activity_grades/activity_grades_POST.xs`)
- **Method & Path**: `POST /activity_grades`
- **Authentication**: `auth = true`
- **Input Parameters**:
  - `activity_id`: `int` (required)
  - `student_id`: `int` (required)
  - `grade`: `decimal` (required, validated: `grade >= 0.0 && grade <= 10.0`)
  - `feedback`: `text?` (optional)
- **Logic**:
  - Capture `professor_id` from `$auth.id`.
  - Validate grade boundaries (0.0 to 10.0).
  - Insert record into `activity_grades`.
  - Return created record.

## Risks / Trade-offs
- **[Out of bounds grades]** → Input validation rejects values `< 0.0` or `> 10.0` with HTTP 422.
- **[Unauthorized grade submissions]** → Enforce authentication and verify instructor credentials.
