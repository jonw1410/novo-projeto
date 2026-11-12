# sync-subjects-tasks Specification

## Purpose
Provide real-time synchronization between EduTrack AI frontend views (Disciplinas and Tarefas) and Xano backend tables (subjects and academic_tasks) with JWT authentication and PDF export capabilities.

## ADDED Requirements

### Requirement: Synchronize Disciplinas Page with Xano
The system SHALL connect the Disciplinas page (`pages/1_📚_Disciplinas.py`) to the Xano `subjects` endpoints using the user's JWT token for authentication, allowing users to list, create, and delete subjects with immediate UI reflection.

#### Scenario: User views subjects list
- **WHEN** an authenticated user opens the Disciplinas page
- **THEN** the system queries Xano `GET /subjects` using the user's Bearer token and renders the user's subjects in the UI.

#### Scenario: User creates a new subject
- **WHEN** an authenticated user submits the new subject form with valid data
- **THEN** the system posts the data to Xano `POST /subjects` using the Bearer token
- **AND** updates the UI state immediately showing the newly created subject.

#### Scenario: User deletes a subject
- **WHEN** an authenticated user chooses to delete an existing subject
- **THEN** the system sends a request to Xano `DELETE /subjects/{id}` with the Bearer token
- **AND** updates the UI state immediately removing the deleted subject.

### Requirement: Synchronize Tarefas Page with Xano
The system SHALL connect the Tarefas page (`pages/2_📝_Tarefas.py`) to the Xano `academic_tasks` endpoints using the user's JWT token, allowing users to view, create, toggle completion status, and delete tasks with immediate UI reflection.

#### Scenario: User views academic tasks
- **WHEN** an authenticated user opens the Tarefas page
- **THEN** the system queries Xano `GET /academic_tasks` and `GET /subjects` using the Bearer token and renders tasks associated with their respective subjects.

#### Scenario: User creates an academic task
- **WHEN** an authenticated user submits a new task form with title and selected subject
- **THEN** the system posts the task data to Xano `POST /academic_tasks` with the Bearer token
- **AND** refreshes the tasks list immediately in the UI.

#### Scenario: User toggles task status
- **WHEN** an authenticated user marks a task status between pending and completed
- **THEN** the system sends a PATCH request to Xano `PATCH /academic_tasks/{id}` with the updated status
- **AND** updates the task display in real time.

#### Scenario: User deletes an academic task
- **WHEN** an authenticated user deletes an academic task
- **THEN** the system sends a DELETE request to Xano `DELETE /academic_tasks/{id}`
- **AND** immediately updates the UI list without manual page reload.

### Requirement: Export Subject and Task Summary to PDF
The system SHALL provide an export action that generates a downloadable PDF file containing the summary of the subject and its associated academic tasks for easy external sharing.

#### Scenario: User exports subject summary to PDF
- **WHEN** an authenticated user clicks the export PDF button for a subject
- **THEN** the system compiles the subject details and related tasks into a PDF document
- **AND** provides an immediate download button for the user to save the PDF.
