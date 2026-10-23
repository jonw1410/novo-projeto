# pages/3_👤_Perfil.py
"""
EduTrack AI – Página de perfil (cadastro e login)

Esta página Streamlit implementa:
  1️⃣ Cadastro de usuário (auth/signup)
  2️⃣ Login (auth/login) → armazena JWT em st.session_state
  3️⃣ Exibição de perfil (auth/me) usando o token armazenado

Requisitos:
  - Arquivo ``.env`` na raiz contendo a variável ``XANO_BASE_URL``
  - Pacotes Python: ``streamlit``, ``python-dotenv`` e ``requests``
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv

# ------------------------------------------------------------
# Carregar configuração da API a partir do .env
# ------------------------------------------------------------
load_dotenv()  # lê .env na raiz do projeto
BASE_URL = os.getenv("XANO_BASE_URL")
if not BASE_URL:
    st.error("⚠️  Variável XANO_BASE_URL não encontrada no .env")
    st.stop()
# Aviso caso ainda seja o placeholder genérico
if "YOUR_XANO_INSTANCE" in BASE_URL:
    st.warning("⚠️  A URL base no .env ainda contém o placeholder `YOUR_XANO_INSTANCE`. Atualize o .env com sua URL real do Xano.")

# Endpoints completos
ENDPOINT_SIGNUP = f"{BASE_URL}/auth/signup"
ENDPOINT_LOGIN = f"{BASE_URL}/auth/login"
ENDPOINT_ME = f"{BASE_URL}/auth/me"

# ------------------------------------------------------------
# Funções auxiliares de chamada à API Xano
# ------------------------------------------------------------
def api_signup(email: str, password: str, name: str) -> dict:
    payload = {"email": email, "password": password, "name": name}
    resp = requests.post(ENDPOINT_SIGNUP, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()

def api_login(email: str, password: str) -> dict:
    payload = {"email": email, "password": password}
    resp = requests.post(ENDPOINT_LOGIN, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()

def api_me(token: str) -> dict:
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(ENDPOINT_ME, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()

# ------------------------------------------------------------
# Interface Streamlit
# ------------------------------------------------------------
st.title("👤 Perfil – Cadastro e Login")

# ---- Seção de Cadastro ----
with st.expander("🟢 Cadastro (Signup)", expanded=False):
    signup_email = st.text_input("Email", key="signup_email")
    signup_name = st.text_input("Nome completo", key="signup_name")
    signup_password = st.text_input("Senha", type="password", key="signup_password")
    if st.button("Cadastrar", key="signup_btn"):
        if not (signup_email and signup_name and signup_password):
            st.error("Preencha todos os campos para cadastrar.")
        else:
            try:
                result = api_signup(signup_email, signup_password, signup_name)
                st.success("✅ Usuário cadastrado com sucesso! Agora faça login.")
            except requests.HTTPError as err:
                st.error(f"Erro ao cadastrar: {err.response.text}")

# ---- Seção de Login ----
with st.expander("🔐 Login", expanded=False):
    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Senha", type="password", key="login_password")
    if st.button("Entrar", key="login_btn"):
        if not (login_email and login_password):
            st.error("Preencha email e senha para fazer login.")
        else:
            try:
                resp = api_login(login_email, login_password)
                token = resp.get("token") or resp.get("jwt")
                if not token:
                    st.error("Login falhou: token não retornado.")
                else:
                    st.session_state["token"] = token
                    st.session_state["user"] = resp.get("user")
                    st.success("✅ Login bem‑sucedido!")
            except requests.HTTPError as err:
                st.error(f"Erro no login: {err.response.text}")

# ---- Seção de Perfil ----
if st.session_state.get("token"):
    with st.expander("📋 Perfil do Usuário", expanded=True):
        try:
            profile = api_me(st.session_state["token"])
            st.json(profile)
        except requests.HTTPError as err:
            st.error(f"Não foi possível obter o perfil: {err.response.text}")
else:
    st.info("🔸 Faça login para visualizar seu perfil.")

"""
EduTrack AI – Página de perfil (cadastro e login)

Esta página Streamlit implementa:
  1️⃣ Cadastro de usuário (auth/signup)
  2️⃣ Login (auth/login) → armazena JWT em st.session_state
  3️⃣ Exibição de perfil (auth/me) usando o token armazenado

Requisitos:
  - Arquivo ``.env`` na raiz contendo a variável ``XANO_BASE_URL``
  - Pacotes Python: ``streamlit``, ``python-dotenv`` e ``requests``
"""

import os
import requests
import streamlit as st
from dotenv import load_dotenv

# ------------------------------------------------------------
# Carregar configuração da API a partir do .env
# ------------------------------------------------------------
load_dotenv()  # lê .env na raiz do projeto
BASE_URL = os.getenv("XANO_BASE_URL")
if not BASE_URL:
    st.error("⚠️  Variável XANO_BASE_URL não encontrada no .env")
    st.stop()

# Endpoints completos
ENDPOINT_SIGNUP = f"{BASE_URL}/auth/signup"
ENDPOINT_LOGIN = f"{BASE_URL}/auth/login"
ENDPOINT_ME = f"{BASE_URL}/auth/me"

# ------------------------------------------------------------
# Funções auxiliares de chamada à API Xano
# ------------------------------------------------------------
def api_signup(email: str, password: str, name: str) -> dict:
    payload = {"email": email, "password": password, "name": name}
    resp = requests.post(ENDPOINT_SIGNUP, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()

def api_login(email: str, password: str) -> dict:
    payload = {"email": email, "password": password}
    resp = requests.post(ENDPOINT_LOGIN, json=payload, timeout=10)
    resp.raise_for_status()
    return resp.json()

def api_me(token: str) -> dict:
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(ENDPOINT_ME, headers=headers, timeout=10)
    resp.raise_for_status()
    return resp.json()

# ------------------------------------------------------------
# Interface Streamlit
# ------------------------------------------------------------
st.title("👤 Perfil – Cadastro e Login")

# ---- Seção de Cadastro ----
with st.expander("🟢 Cadastro (Signup)", expanded=False):
    signup_email = st.text_input("Email", key="signup_email")
    signup_name = st.text_input("Nome completo", key="signup_name")
    signup_password = st.text_input("Senha", type="password", key="signup_password")
    if st.button("Cadastrar", key="signup_btn"):
        if not (signup_email and signup_name and signup_password):
            st.error("Preencha todos os campos para cadastrar.")
        else:
            try:
                result = api_signup(signup_email, signup_password, signup_name)
                st.success("✅ Usuário cadastrado com sucesso! Agora faça login.")
            except requests.HTTPError as err:
                st.error(f"Erro ao cadastrar: {err.response.text}")

# ---- Seção de Login ----
with st.expander("🔐 Login", expanded=False):
    login_email = st.text_input("Email", key="login_email")
    login_password = st.text_input("Senha", type="password", key="login_password")
    if st.button("Entrar", key="login_btn"):
        if not (login_email and login_password):
            st.error("Preencha email e senha para fazer login.")
        else:
            try:
                resp = api_login(login_email, login_password)
                token = resp.get("token") or resp.get("jwt")
                if not token:
                    st.error("Login falhou: token não retornado.")
                else:
                    st.session_state["token"] = token
                    st.session_state["user"] = resp.get("user")
                    st.success("✅ Login bem‑sucedido!")
            except requests.HTTPError as err:
                st.error(f"Erro no login: {err.response.text}")

# ---- Seção de Perfil ----
if st.session_state.get("token"):
    with st.expander("📋 Perfil do Usuário", expanded=True):
        try:
            profile = api_me(st.session_state["token"])
            st.json(profile)
        except requests.HTTPError as err:
            st.error(f"Não foi possível obter o perfil: {err.response.text}")
else:
    st.info("🔸 Faça login para visualizar seu perfil.")

