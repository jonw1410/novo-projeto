## Context

EduTrack AI is a Streamlit academic management application integrating with Xano via REST APIs. Currently, authentication is handled in `pages/3_👤_Perfil.py` where a JWT is obtained and stored in `st.session_state["token"]`. The pages `pages/1_📚_Disciplinas.py` and `pages/2_📝_Tarefas.py` contain mock data. In addition, some Xano query files use `auth = ""` or `auth = "usuarios"` instead of `auth = "user"`, causing the error `This token belongs to a different object type.`

## Goals / Non-Goals

**Goals:**
- Provide full CRUD integration for `subjects` and `academic_tasks` using `st.session_state["token"]`.
- Fix the Xano query files in `api/subjects/` and `api/academic_tasks/` to use `auth = "user"` matching the auth table in `table/user.xs`.
- Ensure instant UI reactivity upon record creation, update, and deletion using Streamlit's state management and `st.rerun()`.
- Add an in-memory, pure-Python PDF generator for subjects and task lists, generating downloadable PDF files without external network dependencies.

**Non-Goals:**
- Modifying database schemas in `table/*.xs`.
- Running automated push/deploy to Xano servers (strictly prohibited per AGENTS.md Rule #2).

## Decisions

1. **Authentication Alignment:**
   - Set `auth = "user"` across all endpoints in `api/subjects/` and `api/academic_tasks/`.
   - Reason: The login endpoint issues tokens for table `user`. Aligning this attribute prevents the "This token belongs to a different object type." error.

2. **UI Reactivity:**
   - Execute API calls in helper functions, capture success, and invoke `st.rerun()` to immediately fetch and display updated records without needing full browser refreshes.

3. **PDF Generation Strategy:**
   - Implement an in-memory PDF 1.4 byte builder function that formats subject metadata, teacher, hours, and related academic tasks into standard PDF syntax.
   - Reason: Works 100% offline in sandbox environments without requiring uninstalled packages or browser-side headless runtimes, while delivering standard PDF files via `st.download_button`.

## Risks / Trade-offs

- **[Unauthenticated Access]** → Display an informative alert with a direct prompt to log in via Perfil (`pages/3_👤_Perfil.py`) if `st.session_state["token"]` is absent.
- **[Network or API Errors]** → Catch `requests.RequestException` gracefully and extract user-friendly error messages from Xano responses.
