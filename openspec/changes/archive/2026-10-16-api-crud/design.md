# Technical Design: api-crud

## Context
See `proposal.md` for background and motivation. This design details the architecture, data schemas, security isolation rules, and endpoint specifications for the CRUD operations of `subjects` and `academic_tasks` in Xano.

## Goals / Non-Goals

**Goals:**
- Provide full RESTful CRUD (POST, GET, PATCH, DELETE) for `subjects`.
- Provide full RESTful CRUD (POST, GET, PATCH, DELETE) for `academic_tasks`.
- Enforce strict user isolation where every query filters or validates against `$auth.id`.
- Define schema for `academic_tasks` in XanoScript (`tables/academic_tasks.xs`).

**Non-Goals (Strict Scope Enforcement per AGENTS.md):**
- DO NOT generate frontend components or modify Streamlit UI.
- DO NOT generate automated test suites.
- DO NOT attempt automated push/sync to Xano Cloud (manual push is developer responsibility).

## Decisions

### 1. Security & Multi-tenant User Isolation
- All endpoints must declare `auth = true`.
- **POST Operations**: Automatically inject `user_id = $auth.id` into the record payload.
- **GET Operations**: All list queries filter by `user_id = $auth.id`.
- **PATCH / DELETE Operations**: Records are fetched and verified by matching both `id = $input.id` AND `user_id = $auth.id`. If no matching record exists for `$auth.id`, the endpoint triggers a `precondition` error (HTTP 404 / Unauthorized).

### 2. Database Schema: `academic_tasks` (`tables/academic_tasks.xs`)
```xanoscript
table academic_tasks {
  auth = false

  schema {
    int id
    timestamp created_at?=now {
      visibility = "private"
    }

    text title filters=trim
    text priority?="Média" filters=trim
    text status?="Pendente" filters=trim
    timestamp? due_date?

    int subject_id {
      table = "subjects"
    }

    int user_id {
      table = "usuarios"
    }
  }

  index = [
    {type: "primary", field: [{name: "id"}]}
    {type: "btree", field: [{name: "user_id", op: "asc"}]}
    {type: "btree", field: [{name: "subject_id", op: "asc"}]}
    {type: "btree", field: [{name: "created_at", op: "desc"}]}
  ]
}
```

### 3. API Endpoints Specification

#### Subjects API Group (`apis/subjects/`)
1. `POST /subjects`: Creates a new subject for the authenticated user (`user_id = $auth.id`).
2. `GET /subjects`: Returns all subjects where `user_id = $auth.id`.
3. `PATCH /subjects/{id}`: Updates name, teacher, or hours for subject `{id}` where `user_id = $auth.id`.
4. `DELETE /subjects/{id}`: Deletes subject `{id}` where `user_id = $auth.id`.

#### Academic Tasks API Group (`apis/academic_tasks/`)
1. `POST /academic_tasks`: Creates a task for the authenticated user (`user_id = $auth.id`).
2. `GET /academic_tasks`: Returns all tasks where `user_id = $auth.id`.
3. `PATCH /academic_tasks/{id}`: Updates title, status, priority, or due_date for task `{id}` where `user_id = $auth.id`.
4. `DELETE /academic_tasks/{id}`: Deletes task `{id}` where `user_id = $auth.id`.

## Risks / Trade-offs
- **[Cross-user Data Tampering]** → Enforced via explicit condition `WHERE id = $input.id AND user_id = $auth.id`.
- **[Foreign Key Violations]** → In `academic_tasks`, verify that the referenced `subject_id` also belongs to `$auth.id`.
