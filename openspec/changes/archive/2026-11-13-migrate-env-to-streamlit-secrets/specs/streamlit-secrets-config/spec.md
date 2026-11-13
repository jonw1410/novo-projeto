# streamlit-secrets-config Specification

## Purpose
Provides native Streamlit secret management for EduTrack AI backend credentials and API endpoints, deprecating direct reliance on local .env files while maintaining environment variable fallback.

## ADDED Requirements

### Requirement: Load Backend Configuration from Streamlit Secrets
The system SHALL read Xano endpoint URLs and application configuration primarily from Streamlit secrets (`st.secrets` backed by `.streamlit/secrets.toml`), allowing smooth execution on Streamlit Community Cloud and local environments.

#### Scenario: Configuration loaded from secrets.toml
- **WHEN** the application starts and valid entries exist in `.streamlit/secrets.toml`
- **THEN** the system reads `XANO_BASE_URL`, `XANO_SUBJECTS_BASE_URL`, and `XANO_TASKS_BASE_URL` directly from `st.secrets`
- **AND** successfully routes API requests to the specified backend endpoints.

#### Scenario: Fallback to environment variables when secret is missing
- **WHEN** a configuration key is not present in `st.secrets` but exists in system environment variables
- **THEN** the system falls back to retrieving the value from `os.getenv` without raising an exception.

### Requirement: Standardized TOML Secrets Formatting
The system SHALL ensure that `.streamlit/secrets.toml` uses valid TOML syntax with double-quoted string values so that Streamlit's secrets parser loads without decoding errors.

#### Scenario: Reading valid TOML secrets
- **WHEN** Streamlit parses `.streamlit/secrets.toml`
- **THEN** all URL definitions are loaded as valid strings and made accessible via `st.secrets`.
