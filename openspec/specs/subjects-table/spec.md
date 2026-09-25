# subjects-table Specification

## Purpose
TBD - created by archiving change create-subjects-table. Update Purpose after archive.

## Requirements

### Requirement: Table Identification and Auth Settings
The table SHALL be named `subjects` and SHALL NOT be an authentication table (`auth = false`).

#### Scenario: Table identification
- **GIVEN** the Xano workspace
- **WHEN** the `subjects` table definition is compiled
- **THEN** the table is named `subjects`
- **AND** `auth` is set to `false`.

### Requirement: Field Definitions
The table SHALL declare the fields: `id` (int primary key), `created_at` (timestamp private), `name` (text with trim), `teacher` (text with trim), `hours` (int), and `user_id` (int foreign key to `usuarios`).

#### Scenario: Successfully creating subject record
- **GIVEN** an authenticated user with `id = 1` in table `usuarios`
- **WHEN** a new subject record is inserted with `name = "Innovation Lab"`, `teacher = "Prof. Ricardo Silva"`, `hours = 80`, `user_id = 1`
- **THEN** Xano assigns an auto-increment `id`
- **AND** sets `created_at = now`
- **AND** trims whitespace on text fields
- **AND** binds the `user_id` foreign key to `usuarios`.

### Requirement: Indexing and Query Performance
The table SHALL declare a primary index on `id`, a btree index on `user_id` (asc), and a btree index on `created_at` (desc).

#### Scenario: Querying subjects by authenticated user
- **GIVEN** multiple subjects registered for different users
- **WHEN** an API query filters by `user_id = $auth.id`
- **THEN** the `btree` index on `user_id` is leveraged for fast indexed retrieval without full table scan.
