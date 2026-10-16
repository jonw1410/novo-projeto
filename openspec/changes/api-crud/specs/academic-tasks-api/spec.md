# academic-tasks-api Specification

## Purpose
Provide secure RESTful CRUD operations for managing academic tasks and assignments in EduTrack AI, enforcing strict authenticated user data isolation.

## ADDED Requirements

### Requirement: Create Academic Task
The system SHALL provide a POST endpoint at `/academic_tasks` requiring authentication to create a task record bound to the authenticated user's ID.

#### Scenario: Successfully creating a task
- **WHEN** an authenticated user sends a POST request to `/academic_tasks` with title, subject_id, due_date, and priority
- **THEN** the system creates the task record with `user_id` set to `$auth.id`
- **AND** returns HTTP 200 with the newly created task record.

### Requirement: List User Tasks
The system SHALL provide a GET endpoint at `/academic_tasks` requiring authentication that returns only tasks owned by the authenticated user.

#### Scenario: Querying user tasks
- **WHEN** an authenticated user sends a GET request to `/academic_tasks`
- **THEN** the system queries the database filtering strictly `WHERE user_id = $auth.id`
- **AND** returns the list of matching tasks.

### Requirement: Update Academic Task
The system SHALL provide a PATCH endpoint at `/academic_tasks/{id}` requiring authentication that allows updating a task only if it belongs to the authenticated user.

#### Scenario: Updating owned task
- **WHEN** an authenticated user sends a PATCH request to `/academic_tasks/{id}` for a record where `user_id = $auth.id`
- **THEN** the system updates the specified fields (e.g. status, priority, title)
- **AND** returns the updated task record.

#### Scenario: Unauthorized update attempt on another user's task
- **WHEN** an authenticated user sends a PATCH request to `/academic_tasks/{id}` for a record owned by a different user
- **THEN** the system rejects the operation with a not found or unauthorized error.

### Requirement: Delete Academic Task
The system SHALL provide a DELETE endpoint at `/academic_tasks/{id}` requiring authentication that removes a task only if owned by the authenticated user.

#### Scenario: Deleting owned task
- **WHEN** an authenticated user sends a DELETE request to `/academic_tasks/{id}` for a record where `user_id = $auth.id`
- **THEN** the system deletes the record
- **AND** returns a success response.
