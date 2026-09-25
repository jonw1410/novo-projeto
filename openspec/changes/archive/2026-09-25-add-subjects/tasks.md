# Implementation Checklist: Add Academic Subjects Management (add-subjects)

- [x] 1. Data Layer & Persistence Setup
  - [x] 1.1 Implement `loadSubjects()` and `saveSubjects()` using `localStorage` with fallback to default Impacta subjects
  - [x] 1.2 Add schema validation for subject records before persisting
  - [x] 1.3 Add reset/restore default subjects utility function

- [x] 2. Subject Registration & Validation
  - [x] 2.1 Enhance the "Cadastrar Nova Disciplina" modal with validation (name, professor, P1, attendance %)
  - [x] 2.2 Calculate initial status ("Aprovado" vs "Atenção") based on P1 >= 7.0 and attendance >= 75%
  - [x] 2.3 Persist newly created subjects and trigger reactive UI refresh

- [x] 3. Subject Editing and Deletion
  - [x] 3.1 Add Edit action to subject cards with pre-populated edit modal
  - [x] 3.2 Implement update logic and save modified subject to storage
  - [x] 3.3 Add Delete action with confirmation prompt and removal from storage

- [x] 4. Metric & UI Synchronization
  - [x] 4.1 Update top KPI cards (Disciplinas Ativas, Média Geral CR, Frequência Global) dynamically
  - [x] 4.2 Re-render performance chart on Canvas with newly added/updated subjects
  - [x] 4.3 Update discipline dropdowns in Task creation modal and AI Grade Simulator

- [x] 5. Verification & Testing
  - [x] 5.1 Test adding a new subject and verifying persistence across browser refresh
  - [x] 5.2 Test editing and deleting a subject
  - [x] 5.3 Verify that the AI Grade Simulator and Task lists correctly reflect updated subjects
