## Why

The EduTrack AI Streamlit frontend currently contains mock data and placeholder tabs on the Disciplinas (`pages/1_📚_Disciplinas.py`) and Tarefas (`pages/2_📝_Tarefas.py`) pages. Students need full synchronization with the Xano backend (`subjects` and `academic_tasks` tables) using their authenticated JWT session, real-time UI state updates upon creating, editing, and deleting records, and the ability to export and share their subjects and task summaries as a PDF document.

## What Changes

- Connect `pages/1_📚_Disciplinas.py` to Xano `subjects` CRUD endpoints using the authenticated JWT token stored in `st.session_state["token"]`.
- Connect `pages/2_📝_Tarefas.py` to Xano `academic_tasks` CRUD endpoints using the authenticated JWT token.
- Update Xano endpoint files in `api/subjects/` and `api/academic_tasks/` to ensure authentication table is configured as `user` (resolving the token object type mismatch).
- Provide immediate UI state reactivity and data refresh upon creating, modifying, and deleting subjects and tasks without requiring manual full page reloads.
- Implement an in-app PDF export functionality allowing users to generate and download a PDF summary of subjects and their associated tasks.

## Capabilities

### New Capabilities
- `sync-subjects-tasks`: End-to-end synchronization between Streamlit frontend pages (Disciplinas and Tarefas) and Xano REST endpoints (`subjects` and `academic_tasks`) with JWT authentication, immediate UI state updates, and PDF export functionality.

## Impact

- **Frontend Pages**: Replaces mock implementations in `pages/1_📚_Disciplinas.py` and `pages/2_📝_Tarefas.py` with dynamic, authenticated Xano API integrations.
- **Backend Endpoints**: Aligns authentication configurations in `api/subjects/*.xs` and `api/academic_tasks/*.xs` with the `user` table.
- **Sharing**: Adds PDF summary export for subjects and task lists.
