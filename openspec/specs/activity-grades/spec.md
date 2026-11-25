# activity-grades Specification

## Purpose

Enable instructors to assign, store, and validate grades and qualitative feedback for students on specific academic activities.

## Requirements

### Requirement: Record Student Activity Grade
The system SHALL record an activity grade submitted by an instructor for a specific student and academic activity.

#### Scenario: Successfully launching a grade for a student
- **WHEN** an instructor submits a valid grade between 0.0 and 10.0 for a student on a specific activity
- **THEN** the system stores the record in the activity_grades table
- **AND** associates the grade with the student ID, activity ID, and instructor ID.

#### Scenario: Validation of invalid grade range
- **WHEN** an instructor submits a grade below 0.0 or above 10.0
- **THEN** the system rejects the submission with a validation error
- **AND** does not create or update any grade record.

### Requirement: Post Activity Grade Endpoint
The system SHALL expose a POST endpoint at `/activity_grades` to receive and process grade submissions.

#### Scenario: Submitting grade via REST API
- **WHEN** an authorized instructor sends a POST request to `/activity_grades` with activity_id, student_id, grade, and optional feedback
- **THEN** the endpoint validates the input payload
- **AND** returns HTTP 200 with the created grade details.
