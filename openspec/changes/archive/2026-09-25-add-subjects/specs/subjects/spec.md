# Subject Management Specification

## ADDED Requirements

### Requirement: Create New Subject
The system SHALL allow students to register a new academic subject with required metadata and initial performance values.

#### Scenario: Successfully adding a subject with valid data
- **GIVEN** a student is on the Disciplinas view or Dashboard
- **WHEN** the student submits the "Adicionar Disciplina" form with name, professor, P1 grade, and attendance percentage
- **THEN** the system creates the new subject record
- **AND** updates the total active subjects count KPI
- **AND** recalculates the overall GPA (CR)
- **AND** updates the performance chart and dropdown selectors in other modules
- **AND** persists the record to storage.

#### Scenario: Validation of required subject fields
- **GIVEN** a student opens the subject creation form
- **WHEN** the student submits without providing a subject name
- **THEN** the system displays a clear validation message
- **AND** does not create an empty record.

---

### Requirement: Persistent Storage of Subjects
The system SHALL persist all registered subjects across page reloads and browser sessions.

#### Scenario: Reloading the application retains added subjects
- **GIVEN** a student has registered a custom subject
- **WHEN** the application page is reloaded or reopened
- **THEN** the persisted subjects are loaded from local storage
- **AND** the state restores all user additions.

---

### Requirement: Delete and Edit Subjects
The system SHALL permit removing or updating an existing subject.

#### Scenario: Deleting a subject
- **GIVEN** a list of registered subjects
- **WHEN** the student confirms deletion of a subject
- **THEN** the subject is removed from the active list and storage
- **AND** dependent metrics (GPA, attendance %, chart) update immediately.

---

### Requirement: Subject Synchronization with Simulator and Tasks
The system SHALL synchronize available subjects with the AI Grade Simulator and Task Manager.

#### Scenario: Dynamic option in selector
- **GIVEN** a student adds a new subject "Engenharia de Prompt"
- **WHEN** the student navigates to "Simulador IA de Notas" or "Nova Tarefa"
- **THEN** "Engenharia de Prompt" is immediately available in the subject selection dropdown.

