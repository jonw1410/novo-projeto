# cadastro-login Specification

## Purpose
Define the front‑end authentication flow for EduTrack AI using existing Xano authentication endpoints (`auth/signup`, `auth/login`, `auth/me`). The implementation consists of a Streamlit page and an environment configuration file.

## ADDED Requirements

### Requirement: Environment Configuration
The system SHALL provide a `.env` file at the project root containing the variable `XANO_BASE_URL` that holds the base URL for all Xano API calls.

#### Scenario: Loading base URL
- **WHEN** the Streamlit page starts,
- **THEN** it loads `XANO_BASE_URL` from the `.env` file using `python‑dotenv`.

### Requirement: User Registration Endpoint
The system SHALL call `POST ${XANO_BASE_URL}/auth/signup` with JSON payload `{email, password, name}` to create a new user in the existing `users` table.

#### Scenario: Successful sign‑up
- **WHEN** a user provides a valid email, password, and name and clicks **Sign Up**,
- **THEN** the request returns HTTP 201 and the UI shows a success message.

### Requirement: User Login Endpoint
The system SHALL call `POST ${XANO_BASE_URL}/auth/login` with JSON payload `{email, password}` to obtain a JWT token.

#### Scenario: Successful login
- **WHEN** a user provides correct credentials and clicks **Log In**,
- **THEN** the request returns a JWT token which is stored in `st.session_state['token']`.

### Requirement: Session Validation Endpoint
The system SHALL call `GET ${XANO_BASE_URL}/auth/me` with header `Authorization: Bearer <token>` to retrieve the authenticated user's profile.

#### Scenario: Profile display
- **WHEN** a valid token exists in session state,
- **THEN** the UI displays the user's `email`, `name`, and `id`.

## Non‑Goals
- No changes to Xano backend tables or scripts.
- No automated tests or CI pipelines.
- No deployment or push to Xano (developer must push manually).

