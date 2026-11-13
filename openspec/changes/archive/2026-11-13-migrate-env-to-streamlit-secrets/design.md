## Context

EduTrack AI application views and utility modules historically loaded configuration variables (`XANO_BASE_URL`, `XANO_SUBJECTS_BASE_URL`, `XANO_TASKS_BASE_URL`) from a `.env` file via `dotenv.load_dotenv()` and `os.getenv()`. To support Streamlit Cloud and standard Streamlit deployments, configuration must be sourced directly from Streamlit's native secrets mechanism (`st.secrets`) backed by `.streamlit/secrets.toml`.

## Goals / Non-Goals

**Goals:**
- Format `.streamlit/secrets.toml` with valid TOML syntax (string values enclosed in double quotes).
- Provide a robust configuration accessor function (`get_config_value`) in `utils/xano_client.py` that prioritizes `st.secrets` and gracefully falls back to `os.getenv`.
- Update `pages/1_📚_Disciplinas.py`, `pages/2_📝_Tarefas.py`, and `pages/3_👤_Perfil.py` to read backend URLs via the unified secrets resolver.

**Non-Goals:**
- Modifying backend Xano tables or `.xs` query files.
- Pushing or deploying code to external servers (per AGENTS.md Rule #2).

## Decisions

1. **Secrets Accessor with Graceful Fallback:**
   - In `utils/xano_client.py`, define `get_config_value(key: str, default: str = "") -> str`.
   - Priority order:
     1. `st.secrets.get(key)` (if running within a Streamlit execution context).
     2. `os.getenv(key)` (for backwards compatibility and CLI execution).
     3. `default` parameter.
   - Rationale: Ensures Streamlit pages load from `st.secrets` while preventing crashes when scripts or tests run outside Streamlit.

2. **Secrets File Syntax Correction:**
   - Format `.streamlit/secrets.toml` with standard TOML key-value pairs:
     ```toml
     XANO_BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:cPkbqL8B"
     XANO_SUBJECTS_BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:WTDGU8XU"
     XANO_TASKS_BASE_URL = "https://x8ki-letl-twmt.n7.xano.io/api:VIQ0W9tI"
     ```

## Risks / Trade-offs

- **[Missing Secrets File in CI/CD]** → The fallback to `os.getenv` prevents breakage in environments where `.streamlit/secrets.toml` is not mounted.
- **[TOML Parsing Error]** → Ensure all URLs are quoted as strings so Streamlit's TOML parser succeeds.
