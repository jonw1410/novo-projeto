# subjects-api Specification

## Purpose
Provide secure RESTful CRUD operations for managing academic subjects in EduTrack AI, enforcing strict authenticated user data isolation.

## ADDED Requirements

### Requirement: Create Subject
The system SHALL provide a POST endpoint at `/subjects` requiring authentication to create a subject record bound to the authenticated user's ID.

#### Scenario: Successfully creating a subject
- **WHEN** an authenticated user sends a POST request to `/subjects` with valid subject data
- **THEN** the system creates the subject record with `user_id` set to `$auth.id`
- **AND** returns HTTP 200 with the newly created subject record.

### Requirement: List User Subjects
The system SHALL provide a GET endpoint at `/subjects` requiring authentication that returns only subjects owned by the authenticated user.

#### Scenario: Querying user subjects
- **WHEN** an authenticated user sends a GET request to `/subjects`
- **THEN** the system queries the database filtering strictly `WHERE user_id = $auth.id`
- **AND** returns the list of matching subjects.

### Requirement: Update Subject
The system SHALL provide a PATCH endpoint at `/subjects/{id}` requiring authentication that allows updating a subject only if it belongs to the authenticated user.

#### Scenario: Updating owned subject
- **WHEN** an authenticated user sends a PATCH request to `/subjects/{id}` for a record where `user_id = $auth.id`
- **THEN** the system updates the specified fields
- **AND** returns the updated record.

#### Scenario: Unauthorized update attempt on another user's subject
- **WHEN** an authenticated user sends a PATCH request to `/subjects/{id}` for a record owned by a different user
- **THEN** the system rejects the operation with a not found or unauthorized error.

### Requirement: Delete Subject
The system SHALL provide a DELETE endpoint at `/subjects/{id}` requiring authentication that removes a subject only if owned by the authenticated user.

#### Scenario: Deleting owned subject
- **WHEN** an authenticated user sends a DELETE request to `/subjects/{id}` for a record where `user_id = $auth.id`
- **THEN** the system deletes the record
- **AND** returns a success response.
