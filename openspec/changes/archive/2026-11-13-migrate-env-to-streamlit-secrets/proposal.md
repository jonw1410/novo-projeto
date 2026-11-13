## Why

EduTrack AI currently relies on `.env` files parsed via `python-dotenv` for backend API configuration (`XANO_BASE_URL`, `XANO_SUBJECTS_BASE_URL`, `XANO_TASKS_BASE_URL`). Migrating configuration management to Streamlit's native `st.secrets` (`.streamlit/secrets.toml`) follows Streamlit Cloud and local production best practices, standardizes secret handling across pages, and prevents runtime dependency on `.env` files while maintaining graceful backwards compatibility.

## What Changes

- Format and populate `.streamlit/secrets.toml` with valid TOML syntax for `XANO_BASE_URL`, `XANO_SUBJECTS_BASE_URL`, and `XANO_TASKS_BASE_URL`.
- Create a centralized secrets and configuration resolver (`get_config_value`) supporting Streamlit `st.secrets` with fallback to `os.getenv`.
- Update `utils/xano_client.py` to retrieve Xano API endpoint URLs primarily from `st.secrets`.
- Update `pages/1_📚_Disciplinas.py`, `pages/2_📝_Tarefas.py`, and `pages/3_👤_Perfil.py` to source backend endpoints through the centralized secrets loader.

## Capabilities

### New Capabilities
- `streamlit-secrets-config`: Native configuration and secret loading via Streamlit secrets (`st.secrets` / `.streamlit/secrets.toml`) with fallback support for environment variables.

## Impact

- **Configuration Files**: Corrects `.streamlit/secrets.toml` to standard TOML syntax.
- **Client Pages & Utils**: Migrates `utils/xano_client.py`, `pages/1_📚_Disciplinas.py`, `pages/2_📝_Tarefas.py`, and `pages/3_👤_Perfil.py` from direct `dotenv` usage to `st.secrets`.
