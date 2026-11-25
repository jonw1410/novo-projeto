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

BASE_URL = get_config_value("XANO_BASE_URL", "").rstrip("/") or "https://x8ki-letl-twmt.n7.xano.io/api:cPkbqL8B"

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
# Initialize session state keys
if "token" not in st.session_state:
    st.session_state["token"] = None
if "user" not in st.session_state:
    st.session_state["user"] = None

# If user is already authenticated
if st.session_state.get("token"):
    st.title("👤 Meu Perfil")
    user_token = st.session_state["token"]

    st.success("✅ **Sessão Ativa:** Conectado com sucesso ao backend Xano.")

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

        st.markdown(f"**👤 Nome:** `{user_name}`")
        st.markdown(f"**📧 E-mail:** `{user_email}`")
        st.markdown(f"**🆔 ID do Usuário:** `{user_id}`")
        st.markdown(f"**🎓 Função / Papel:** `{user_role}`")

    with col2:
        st.write("")
        st.write("")
        if st.button("🚪 Sair da Conta (Logout)", type="secondary", use_container_width=True):
            st.session_state["token"] = None
            st.session_state["user"] = None
            st.rerun()

    with st.expander("🔍 Detalhes Técnicos da Conta (JSON retornado pelo Xano)"):
        st.json(profile_data)

else:
    # Not authenticated: Prominent, Centered Login & Signup Hero Layout
    col_l, col_center, col_r = st.columns([1, 4, 1])

    with col_center:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 2rem;">
            <div style="display: inline-flex; align-items: center; gap: 8px; padding: 6px 20px; border-radius: 9999px; background: rgba(71, 201, 176, 0.12); border: 1px solid rgba(103, 211, 197, 0.55); color: #A7F3E9; font-weight: 700; font-size: 0.95rem; margin-bottom: 14px; letter-spacing: 1px;">
                <span>✨</span> AUTENTICAÇÃO EDUTRACK AI
            </div>
            <h1 style="font-size: 2.8rem; font-weight: 800; background: linear-gradient(120deg, #F8FAFC 0%, #C8E7E3 55%, #67D3C5 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin: 0; filter: drop-shadow(0 6px 18px rgba(2, 8, 23, 0.3));">
                Acesse sua Conta
            </h1>
            <p style="color: #A9B9CC; font-size: 1.15rem; margin-top: 10px; font-weight: 500;">
                Faça login ou crie sua conta para gerenciar notas, disciplinas e tarefas acadêmicas.
            </p>
        </div>
        """, unsafe_allow_html=True)

        tab_login, tab_signup = st.tabs(["🔐 ENTRAR (LOGIN)", "✨ CRIAR CONTA (CADASTRO)"])

        # --- TAB LOGIN ---
        with tab_login:
            st.markdown("""
            <div style="margin: 1rem 0 1.2rem 0;">
                <h3 style="color: #A7F3E9; font-size: 1.45rem; font-weight: 750; margin: 0;">🔐 Acessar Minha Conta</h3>
                <p style="color: #A9B9CC; font-size: 0.98rem; margin: 4px 0 0 0;">Informe seu e-mail e senha cadastrados para entrar:</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("form_login"):
                login_email = st.text_input("📧 Seu E-mail", placeholder="seu-email@exemplo.com", key="input_login_email")
                login_password = st.text_input("🔑 Sua Senha", type="password", placeholder="Digite sua senha", key="input_login_password")
                submit_login = st.form_submit_button("🚀 ENTRAR NA PLATAFORMA", type="primary", use_container_width=True)

                if submit_login:
                    if not login_email or not login_password:
                        st.warning("⚠️ Por favor, preencha o e-mail e a senha.")
                    else:
                        try:
                            with st.spinner("Autenticando no Xano..."):
                                auth_response = api_login(login_email, login_password)
                                token = auth_response.get("authToken") or auth_response.get("token") or auth_response.get("jwt")

                                if not token:
                                    st.error("❌ Falha na autenticação: token não retornado pelo servidor.")
                                else:
                                    st.session_state["token"] = token
                                    st.success("✅ Login realizado com sucesso!")
                                    st.rerun()
                        except requests.RequestException as exc:
                            st.error(f"❌ Falha no login: {extract_error_message(exc)}")

        # --- TAB SIGNUP ---
        with tab_signup:
            st.markdown("""
            <div style="margin: 1rem 0 1.2rem 0;">
                <h3 style="color: #A7F3E9; font-size: 1.45rem; font-weight: 750; margin: 0;">✨ Criar Nova Conta</h3>
                <p style="color: #A9B9CC; font-size: 0.98rem; margin: 4px 0 0 0;">Preencha os dados abaixo para registrar-se no EduTrack AI:</p>
            </div>
            """, unsafe_allow_html=True)

            with st.form("form_signup"):
                signup_name = st.text_input("👤 Nome Completo", placeholder="Seu nome completo", key="input_signup_name")
                signup_email = st.text_input("📧 E-mail para Cadastro", placeholder="seu-email@exemplo.com", key="input_signup_email")
                signup_password = st.text_input("🔒 Senha de Acesso", type="password", placeholder="Crie uma senha segura", key="input_signup_password")
                submit_signup = st.form_submit_button("✨ FINALIZAR CADASTRO", type="primary", use_container_width=True)

                if submit_signup:
                    if not signup_name or not signup_email or not signup_password:
                        st.warning("⚠️ Por favor, preencha todos os campos para se cadastrar.")
                    else:
                        try:
                            with st.spinner("Criando conta no Xano..."):
                                signup_response = api_signup(signup_name, signup_email, signup_password)
                                token = signup_response.get("authToken") or signup_response.get("token") or signup_response.get("jwt")

                                if token:
                                    st.session_state["token"] = token
                                    st.success("✅ Cadastro realizado com sucesso! Conectando à sua conta...")
                                    st.rerun()
                                else:
                                    st.success("✅ Cadastro realizado com sucesso! Vá para a aba 'Entrar' e faça login.")
                        except requests.RequestException as exc:
                            st.error(f"❌ Erro no cadastro: {extract_error_message(exc)}")

