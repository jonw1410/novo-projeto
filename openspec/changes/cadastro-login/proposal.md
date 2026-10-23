# Change: cadastro-login

## Why
Users need to be able to create an account and authenticate to access their personalized data in EduTrack AI. Providing a simple Python UI page that interacts with the existing Xano authentication endpoints (`auth/signup`, `auth/login`, `auth/me`) enables rapid onboarding and secure session handling.

## What Changes
- Add a `.env` file in the project root to store the base URL for Xano API endpoints.
- Create a new Streamlit (or plain Python) page `pages/3_👤_Perfil.py` that implements signup, login, and session retrieval using the Xano endpoints.
- Use the existing `users` table (Xano) to persist registration data.
- Ensure the script respects multi‑tenant isolation by always sending the authenticated user ID (`$auth.id`) when accessing protected resources.

## Capabilities
- **User Registration** (`POST auth/signup`)
- **User Login** (`POST auth/login`)
- **Session Validation** (`GET auth/me`)
- **Secure storage** of the base API URL in `.env`.

## Impact
- Adds front‑end logic for authentication.
- No changes to backend schemas; existing `users` table is reused.
- Front‑end code will be local; deployment is manual (developer responsibility).
