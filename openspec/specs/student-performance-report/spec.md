# student-performance-report Specification

## Purpose
Provides automated generation and download of academic performance PDF reports for students, compiling enrolled subjects, completed tasks, and progress indicators.

## Requirements

### Requirement: Generate Student Performance PDF Script
The system SHALL provide a standalone Python script to generate a student academic performance report in PDF format, summarizing subjects, completed and pending tasks, and global completion statistics.

#### Scenario: Script generates performance report
- **WHEN** the performance report script is executed with student data or an active session token
- **THEN** the script compiles all academic metrics and outputs a structured PDF file on the local file system.

#### Scenario: Script handles student with no tasks
- **WHEN** the script processes a student who has enrolled subjects but zero registered tasks
- **THEN** the script produces a valid PDF indicating that no tasks are registered with a 0% completion rate.

### Requirement: Xano Endpoint to Download Performance Report
The system SHALL provide an authenticated Xano API endpoint that allows an authenticated student to request and download their academic performance report file or payload.

#### Scenario: Authenticated user requests performance report download
- **WHEN** an authenticated user calls the performance report download endpoint with a valid Bearer token
- **THEN** the system verifies user identity using the authenticated user ID (`$auth.id`)
- **AND** returns the performance report data or downloadable file payload scoped strictly to that user.

#### Scenario: Unauthenticated request to download performance report
- **WHEN** a request without an authentication token is sent to the report download endpoint
- **THEN** the system rejects the request with HTTP 401 Unauthorized.
