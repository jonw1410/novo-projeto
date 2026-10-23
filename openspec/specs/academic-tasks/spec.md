# academic-tasks Specification

## Purpose
Define the `academic_tasks` table so that students can register and manage their academic obligations (assignments, exams, projects) linked to each subject.

## Requirements

### Requirement: Store academic tasks
The system SHALL allow each authenticated user to create, retrieve, update, and delete academic task records linked to a subject.

#### Scenario: Create a new academic task
- **WHEN** the user sends a POST request to `/academic_tasks` with `title`, `description`, `due_date`, `status`, and `subject_id`
- **THEN** a new `academic_tasks` record is created associated with the requesting `user_id`.

#### Scenario: List a user's academic tasks
- **WHEN** the user sends a GET request to `/academic_tasks`
- **THEN** the system returns only the tasks where `user_id` matches the authenticated user.

#### Scenario: Update an academic task
- **WHEN** the user sends a PATCH request to `/academic_tasks/{id}` with any mutable fields
- **THEN** the system updates the specified task if it belongs to the user.

#### Scenario: Delete an academic task
- **WHEN** the user sends a DELETE request to `/academic_tasks/{id}`
- **THEN** the system removes the task if it belongs to the user.
