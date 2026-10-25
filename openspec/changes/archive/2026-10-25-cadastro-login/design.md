# Technical Design: cadastro-login

## Context
The platform needs a simple user onboarding flow. Existing Xano authentication endpoints (`auth/signup`, `auth/login`, `auth/me`) and the `users` table will be used. The UI will be a Streamlit page located at `pages/3_👤_Perfil.py`.

## Goals / Non‑Goals

**Goals:**
- Store the base Xano API URL in a `.env` file at the project root.
- Implement a Streamlit page that lets a user **sign‑up**, **log‑in**, and **view their profile** by calling the three Xano endpoints.
- Use the existing `users` (or `usuarios`) table for registration data – no new tables are created.
- Keep the code self‑contained; any required Python packages (e.g., `requests`, `python‑dotenv`, `streamlit`) are assumed to be added manually by the developer.

**Non‑Goals (strict scope enforcement per AGENTS.md):**
- No changes to backend schemas or Xano scripts.
- No automated tests or CI pipelines.
- No push/sync to Xano; deployment is manual.
- No UI beyond the single Streamlit page.

## Decisions

### 1. Environment configuration
- Create a `.env` file with a single variable `XANO_BASE_URL` (e.g., `https://your-xano-instance.com/api`).
- The script will load this file using `python‑dotenv`.

### 2. Streamlit page structure (`pages/3_👤_Perfil.py`)
- Import `os`, `requests`, `streamlit as st`, and `load_dotenv`.
- Provide three sections:
  1. **Sign‑up** – collects `email`, `password`, `name` and POSTs to `${XANO_BASE_URL}/auth/signup`.
  2. **Login** – collects `email`, `password` and POSTs to `${XANO_BASE_URL}/auth/login`; stores the returned JWT in `st.session_state['token']`.
  3. **Profile** – when a token is present, performs a GET to `${XANO_BASE_URL}/auth/me` with `Authorization: Bearer <token>` and displays user info.
- Error handling: display `st.error` on failed requests; success messages with `st.success`.
- All requests use `json=` payloads for POST and appropriate headers for GET.

### 3. Security considerations
- The JWT is kept only in the Streamlit session state (in‑memory) – not persisted to disk.
- The `.env` file must never be committed; developers should add it to `.gitignore` manually if needed.

## Risks / Trade‑offs
- **Token leakage** – The token lives only in session memory; if the user refreshes the page, they must log in again.
- **Dependency management** – The developer must ensure `python‑dotenv`, `requests` and `streamlit` are installed (e.g., via `pip install`), but the agent will not run installs.
- **Network failures** – Simple retry logic could be added later; currently a single request is attempted.

---
All design decisions respect the EduTrack AI rules and keep the scope limited to front‑end authentication functionality.

