"""
EduTrack AI - Profile, Registration and Login Page
Allows users to register, log in, and view profile details via Xano authentication endpoints.
"""

import os
import sys
from typing import Any, Dict
import requests
import streamlit as st

# Ensure root directory is in sys.path for utils import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.xano_client import get_config_value
from utils.ui_theme import apply_custom_theme

# ------------------------------------------------------------
# Environment & Configuration (Streamlit Secrets with fallback)
# ------------------------------------------------------------
st.set_page_config(page_title="Perfil - EduTrack AI", page_icon="👤")
apply_custom_theme()

BASE_URL = get_config_value("XANO_BASE_URL", "").rstrip("/")

if not BASE_URL:
    st.error("⚠️ Configuração `XANO_BASE_URL` não encontrada no `.streamlit/secrets.toml` nem nas variáveis de ambiente.")
    st.info("Por favor, configure `XANO_BASE_URL` no arquivo `.streamlit/secrets.toml`.")
    st.stop()

ENDPOINT_SIGNUP = f"{BASE_URL}/auth/signup"
ENDPOINT_LOGIN = f"{BASE_URL}/auth/login"
ENDPOINT_ME = f"{BASE_URL}/auth/me"


# ------------------------------------------------------------
# Helper API Functions (English naming per EduTrack standards)
# ------------------------------------------------------------
def extract_error_message(err: requests.RequestException) -> str:
    """Extract human-readable error message from response or exception."""
    if hasattr(err, "response") and err.response is not None:
        try:
            error_data = err.response.json()
            if isinstance(error_data, dict):
                return error_data.get("message") or error_data.get("error") or str(error_data)
        except Exception:
            return err.response.text or str(err)
    return str(err)


def api_signup(name: str, email: str, password: str) -> Dict[str, Any]:
    """Register a new user in the Xano user table."""
    payload = {"name": name.strip(), "email": email.strip().lower(), "password": password}
    response = requests.post(ENDPOINT_SIGNUP, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def api_login(email: str, password: str) -> Dict[str, Any]:
    """Authenticate user credentials and retrieve token."""
    payload = {"email": email.strip().lower(), "password": password}
    response = requests.post(ENDPOINT_LOGIN, json=payload, timeout=10)
    response.raise_for_status()
    return response.json()


def api_get_profile(token: str) -> Dict[str, Any]:
    """Fetch authenticated user profile details from Xano."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(ENDPOINT_ME, headers=headers, timeout=10)
    response.raise_for_status()
    return response.json()


# ------------------------------------------------------------
# Streamlit Interface
# ------------------------------------------------------------
st.title("👤 Perfil do Usuário")

# Initialize session state keys
if "token" not in st.session_state:
    st.session_state["token"] = None
if "user" not in st.session_state:
    st.session_state["user"] = None

# If user is already authenticated
if st.session_state.get("token"):
    user_token = st.session_state["token"]

    st.success("✅ Sessão ativa com o backend Xano.")

    # Fetch fresh profile data
    try:
        profile_data = api_get_profile(user_token)
        st.session_state["user"] = profile_data
    except requests.RequestException as exc:
        st.error(f"Erro ao carregar perfil: {extract_error_message(exc)}")
        profile_data = st.session_state.get("user") or {}

    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader("📋 Dados da Conta")
        user_name = profile_data.get("name", "Usuário")
        user_email = profile_data.get("email", "-")
        user_id = profile_data.get("id", "-")
        user_role = profile_data.get("role", "student")

        st.markdown(f"**Nome:** {user_name}")
        st.markdown(f"**E-mail:** {user_email}")
        st.markdown(f"**ID do Usuário:** `{user_id}`")
        st.markdown(f"**Função / Role:** `{user_role}`")

    with col2:
        st.write("")
        st.write("")
        if st.button("🚪 Sair (Logout)", type="secondary", use_container_width=True):
            st.session_state["token"] = None
            st.session_state["user"] = None
            st.rerun()

    with st.expander("🔍 Detalhes Técnicos (JSON retornado pelo Xano)"):
        st.json(profile_data)

else:
    # Not authenticated: Show Login & Signup tabs
    tab_login, tab_signup = st.tabs(["🔐 Entrar (Login)", "🟢 Criar Conta (Cadastro)"])

    # --- TAB LOGIN ---
    with tab_login:
        st.subheader("Acesse sua conta")
        with st.form("form_login"):
            login_email = st.text_input("E-mail", placeholder="seu-email@exemplo.com", key="input_login_email")
            login_password = st.text_input("Senha", type="password", placeholder="Digite sua senha", key="input_login_password")
            submit_login = st.form_submit_button("Entrar", type="primary")

            if submit_login:
                if not login_email or not login_password:
                    st.warning("Por favor, preencha o e-mail e a senha.")
                else:
                    try:
                        with st.spinner("Autenticando..."):
                            auth_response = api_login(login_email, login_password)
                            token = auth_response.get("authToken") or auth_response.get("token") or auth_response.get("jwt")

                            if not token:
                                st.error("Erro na autenticação: token não retornado pelo servidor.")
                            else:
                                st.session_state["token"] = token
                                st.success("Login realizado com sucesso!")
                                st.rerun()
                    except requests.RequestException as exc:
                        st.error(f"Falha no login: {extract_error_message(exc)}")

    # --- TAB SIGNUP ---
    with tab_signup:
        st.subheader("Cadastre-se no EduTrack AI")
        with st.form("form_signup"):
            signup_name = st.text_input("Nome Completo", placeholder="Seu nome completo", key="input_signup_name")
            signup_email = st.text_input("E-mail", placeholder="seu-email@exemplo.com", key="input_signup_email")
            signup_password = st.text_input("Senha", type="password", placeholder="Crie uma senha segura", key="input_signup_password")
            submit_signup = st.form_submit_button("Criar Conta", type="primary")

            if submit_signup:
                if not signup_name or not signup_email or not signup_password:
                    st.warning("Por favor, preencha todos os campos para se cadastrar.")
                else:
                    try:
                        with st.spinner("Criando conta..."):
                            signup_response = api_signup(signup_name, signup_email, signup_password)
                            token = signup_response.get("authToken") or signup_response.get("token") or signup_response.get("jwt")

                            if token:
                                st.session_state["token"] = token
                                st.success("✅ Cadastro realizado com sucesso! Conectando à sua conta...")
                                st.rerun()
                            else:
                                st.success("✅ Cadastro realizado com sucesso! Vá para a aba 'Entrar' e faça login.")
                    except requests.RequestException as exc:
                        st.error(f"Erro no cadastro: {extract_error_message(exc)}")

