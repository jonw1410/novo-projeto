# calculate-progress Specification

## Purpose
Define the business logic for calculating subject progress based on task completion in EduTrack AI, exposing the metric via a structured JSON output produced by `scripts/calculate_progress.py`.

## Requirements

### Requirement: Retrieve Tasks from CRUD Endpoint
The system SHALL retrieve academic tasks from the CRUD endpoint (`GET /academic_tasks`) using authenticated API credentials.

#### Scenario: Successful task retrieval
- **WHEN** the script requests tasks for calculation
- **THEN** the system receives the user task list including status and `subject_id` associations.

---

### Requirement: Calculate Progress Percentage for Subject
The system SHALL calculate the progress percentage of a given subject as `(completed_tasks / total_tasks) * 100`, returning `0.0` when total tasks is zero.

#### Scenario: Subject with completed and pending tasks
- **WHEN** a subject has 4 total tasks and 2 are marked as completed
- **THEN** the calculated progress percentage SHALL be `50.0`.

#### Scenario: Subject with no tasks
- **WHEN** a subject has 0 registered tasks
- **THEN** the calculated progress percentage SHALL be `0.0`.

---

### Requirement: JSON Output Generation
The system SHALL output the calculated progress result formatted as valid JSON containing `subject_id`, `total_tasks`, `completed_tasks`, and `progress_percentage`.

#### Scenario: Returning progress payload
- **WHEN** progress calculation completes for a subject
- **THEN** the system outputs a valid JSON string with completion statistics.
