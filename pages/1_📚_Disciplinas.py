"""
EduTrack AI - Disciplinas (Subjects Management)
Full Xano synchronization with JWT authentication, real-time UI updates,
smart URL resolution with fallback, detailed diagnostics, and PDF export.
"""

import os
import sys
from typing import Any, Dict, List
import requests
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Ensure root directory is in sys.path for utils import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.pdf_generator import build_pdf_document
from utils.xano_client import get_endpoint_urls, parse_xano_error, request_with_fallback
from utils.ui_theme import apply_custom_theme

load_dotenv()

st.set_page_config(page_title="Disciplinas - EduTrack AI", page_icon="📚", layout="wide")
apply_custom_theme()

# ------------------------------------------------------------
# Backend Configuration & URLs
# ------------------------------------------------------------
urls = get_endpoint_urls()
URL_SUBJECTS_PRIMARY = f"{urls['subjects']}/subjects"
URL_SUBJECTS_FALLBACK = f"{urls['fallback_subjects']}"
URL_TASKS_PRIMARY = f"{urls['tasks']}/academic_tasks"
URL_TASKS_FALLBACK = f"{urls['fallback_tasks']}"


# ------------------------------------------------------------
# Helper API Functions
# ------------------------------------------------------------
def api_get_subjects(token: str) -> List[Dict[str, Any]]:
    """Retrieve all subjects belonging to the authenticated user."""
    headers = {"Authorization": f"Bearer {token}"}
    resp, _ = request_with_fallback("GET", URL_SUBJECTS_PRIMARY, URL_SUBJECTS_FALLBACK, headers)
    resp.raise_for_status()
    data = resp.json()
    return data if isinstance(data, list) else []


def api_create_subject(token: str, name: str, teacher: str, hours: int) -> Dict[str, Any]:
    """Create a new subject record in Xano."""
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "name": name.strip(),
        "teacher": teacher.strip(),
        "hours": hours,
    }
    resp, _ = request_with_fallback("POST", URL_SUBJECTS_PRIMARY, URL_SUBJECTS_FALLBACK, headers, json_data=payload)
    resp.raise_for_status()
    return resp.json()


def api_delete_subject(token: str, subject_id: int) -> bool:
    """Delete a subject record owned by the authenticated user."""
    headers = {"Authorization": f"Bearer {token}"}
    url_prim = f"{urls['subjects']}/subjects/{subject_id}"
    url_fall = f"{urls['fallback_subjects']}/{subject_id}"
    resp, _ = request_with_fallback("DELETE", url_prim, url_fall, headers)
    resp.raise_for_status()
    return True


def api_get_tasks(token: str) -> List[Dict[str, Any]]:
    """Retrieve all academic tasks belonging to the authenticated user."""
    headers = {"Authorization": f"Bearer {token}"}
    resp, _ = request_with_fallback("GET", URL_TASKS_PRIMARY, URL_TASKS_FALLBACK, headers)
    resp.raise_for_status()
    data = resp.json()
    return data if isinstance(data, list) else []


def render_error_diagnostics(exc: requests.RequestException):
    """Render friendly error message and technical diagnostics."""
    diag = parse_xano_error(exc)
    st.error(f"❌ **Erro de conexão com o Xano:** {diag['message']}")
    if diag.get("hint"):
        st.warning(f"💡 **Como resolver:** {diag['hint']}")
        
    with st.expander("🛠️ Detalhes Técnicos da Requisição"):
        st.markdown(f"- **Código HTTP:** `{diag.get('status_code') or 'Sem resposta'}`")
        st.markdown(f"- **URL Primária:** `{URL_SUBJECTS_PRIMARY}`")
        st.markdown(f"- **URL Fallback:** `{URL_SUBJECTS_FALLBACK}`")
        st.markdown(f"- **Token presente na sessão:** `{'Sim (ativo)' if st.session_state.get('token') else 'Não (faça login no Perfil)'}`")


# ------------------------------------------------------------
# Authentication Guard
# ------------------------------------------------------------
user_token = st.session_state.get("token")

st.title("📚 Gestão de Disciplinas")

if not user_token:
    st.warning("🔒 **Acesso restrito:** Você precisa estar autenticado para gerenciar suas disciplinas.")
    st.info("Por favor, acesse a página de **👤 Perfil** no menu lateral para fazer login ou criar sua conta.")
    st.stop()

# ------------------------------------------------------------
# Real-Time Data Fetch
# ------------------------------------------------------------
subjects_data: List[Dict[str, Any]] = []
fetch_error = None

try:
    with st.spinner("Sincronizando disciplinas com o Xano..."):
        subjects_data = api_get_subjects(user_token)
except requests.RequestException as exc:
    fetch_error = exc

if fetch_error:
    render_error_diagnostics(fetch_error)

# Fetch tasks for associations and PDF reporting
tasks_data: List[Dict[str, Any]] = []
try:
    tasks_data = api_get_tasks(user_token)
except requests.RequestException:
    tasks_data = []

# ------------------------------------------------------------
# Page Tabs
# ------------------------------------------------------------
tab_list, tab_new, tab_export, tab_config = st.tabs([
    "📋 Minhas Disciplinas", 
    "➕ Nova Disciplina", 
    "📄 Exportar / Compartilhar em PDF",
    "⚙️ Diagnóstico de Conexão"
])

# --- TAB 1: LIST / MANAGEMENT ---
with tab_list:
    col_hdr, col_ref = st.columns([4, 1])
    with col_hdr:
        st.subheader("Disciplinas Cadastradas")
    with col_ref:
        if st.button("🔄 Atualizar", use_container_width=True):
            st.rerun()

    if not subjects_data:
        if not fetch_error:
            st.info("Nenhuma disciplina cadastrada até o momento. Utilize a aba **➕ Nova Disciplina** para cadastrar a primeira!")
    else:
        # Metrics summary
        total_subjects = len(subjects_data)
        total_hours = sum(int(s.get("hours") or 0) for s in subjects_data)
        avg_hours = total_hours / total_subjects if total_subjects > 0 else 0

        m1, m2, m3 = st.columns(3)
        m1.metric("Total de Disciplinas", total_subjects)
        m2.metric("Carga Horária Total", f"{total_hours} h")
        m3.metric("Média por Disciplina", f"{avg_hours:.1f} h")

        st.markdown("---")

        # Table View
        df_display = pd.DataFrame([
            {
                "ID": s.get("id"),
                "Disciplina": s.get("name"),
                "Professor": s.get("teacher"),
                "Carga Horária": f"{s.get('hours', 0)} h",
            }
            for s in subjects_data
        ])
        st.dataframe(df_display, use_container_width=True, hide_index=True)

        st.markdown("### ⚙️ Detalhes e Ações por Disciplina")
        for subj in subjects_data:
            s_id = subj.get("id")
            s_name = subj.get("name")
            s_teacher = subj.get("teacher")
            s_hours = subj.get("hours")

            # Associated tasks for this subject
            related_tasks = [t for t in tasks_data if t.get("subject_id") == s_id]

            with st.expander(f"📘 **{s_name}** — Prof. {s_teacher} ({s_hours}h) | {len(related_tasks)} tarefas"):
                c_info, c_action = st.columns([3, 1])
                with c_info:
                    st.write(f"**ID no Xano:** `{s_id}`")
                    st.write(f"**Professor(a):** {s_teacher}")
                    st.write(f"**Carga Horária:** {s_hours} horas")
                    st.write(f"**Tarefas vinculadas:** {len(related_tasks)}")
                    if related_tasks:
                        for rt in related_tasks:
                            st.write(f"- 📌 {rt.get('title')} (Status: `{rt.get('status', 'Pendente')}`)")
                    else:
                        st.caption("Nenhuma tarefa vinculada ainda.")

                with c_action:
                    # Quick PDF Download for this subject
                    sub_meta = {
                        "Disciplina": str(s_name),
                        "Professor": str(s_teacher),
                        "Carga Horaria": f"{s_hours} horas",
                        "Total de Tarefas": str(len(related_tasks)),
                    }
                    sec_items = [
                        {
                            "header": t.get("title", "Sem titulo"),
                            "detail": f"Status: {t.get('status', 'Pendente')} | Prazo: {t.get('due_date') or 'Nao definido'}"
                        }
                        for t in related_tasks
                    ]
                    pdf_bytes = build_pdf_document(
                        title=f"EduTrack AI - {s_name}",
                        subtitle="Resumo da disciplina e tarefas vinculadas",
                        metadata=sub_meta,
                        sections=[{"title": "Tarefas Academicas", "items": sec_items}]
                    )
                    st.download_button(
                        label="📄 Baixar PDF",
                        data=pdf_bytes,
                        file_name=f"disciplina_{s_id}_{str(s_name).lower().replace(' ', '_')}.pdf",
                        mime="application/pdf",
                        key=f"dl_pdf_{s_id}",
                        use_container_width=True,
                    )

                    st.write("")
                    # Delete action
                    if st.button("🗑️ Excluir", key=f"del_subj_{s_id}", type="secondary", use_container_width=True):
                        try:
                            api_delete_subject(user_token, s_id)
                            st.toast(f"Disciplina '{s_name}' excluída com sucesso!", icon="🗑️")
                            st.rerun()
                        except requests.RequestException as exc:
                            render_error_diagnostics(exc)

# --- TAB 2: CREATE SUBJECT ---
with tab_new:
    st.subheader("Cadastrar Nova Disciplina")
    st.caption("Preencha as informações da matéria. O registro será sincronizado diretamente com sua conta no Xano.")

    with st.form("form_create_subject", clear_on_submit=True):
        f_name = st.text_input("Nome da Disciplina *", placeholder="Ex: Algoritmos e Estruturas de Dados")
        f_teacher = st.text_input("Nome do Professor *", placeholder="Ex: Dr. Roberto Guimarães")
        f_hours = st.number_input("Carga Horária (horas) *", min_value=1, max_value=400, value=60, step=10)

        submitted = st.form_submit_button("💾 Salvar Disciplina", type="primary")

        if submitted:
            if not f_name.strip() or not f_teacher.strip():
                st.warning("Por favor, preencha o nome da disciplina e o nome do professor.")
            else:
                try:
                    with st.spinner("Salvando disciplina no Xano..."):
                        api_create_subject(user_token, f_name, f_teacher, int(f_hours))
                        st.success(f"✅ Disciplina '{f_name}' cadastrada com sucesso no Xano!")
                        st.rerun()
                except requests.RequestException as exc:
                    render_error_diagnostics(exc)

# --- TAB 3: PDF EXPORT & SHARING ---
with tab_export:
    st.subheader("📄 Exportar e Compartilhar Resumo em PDF")
    st.caption("Gere um documento PDF elegante e pronto para impressão ou compartilhamento com colegas e orientadores.")

    if not subjects_data:
        st.info("Cadastre ao menos uma disciplina para gerar relatórios em PDF.")
    else:
        subject_options = {f"{s.get('name')} (ID: {s.get('id')})": s for s in subjects_data}
        selected_label = st.selectbox("Selecione a disciplina para exportar:", list(subject_options.keys()))
        selected_subject = subject_options[selected_label]

        sel_id = selected_subject.get("id")
        sel_name = selected_subject.get("name")
        sel_teacher = selected_subject.get("teacher")
        sel_hours = selected_subject.get("hours")

        sel_tasks = [t for t in tasks_data if t.get("subject_id") == sel_id]

        st.markdown("#### Pré-visualização dos Dados")
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"**Disciplina:** {sel_name}")
            st.markdown(f"**Professor(a):** {sel_teacher}")
            st.markdown(f"**Carga Horária:** {sel_hours} horas")
        with c2:
            st.markdown(f"**Total de Tarefas:** {len(sel_tasks)}")
            pending_count = sum(1 for t in sel_tasks if t.get("status") != "Concluída")
            st.markdown(f"**Tarefas Pendentes:** {pending_count}")

        # PDF Compilation
        full_meta = {
            "Disciplina": str(sel_name),
            "Professor": str(sel_teacher),
            "Carga Horaria": f"{sel_hours} horas",
            "Total de Tarefas": str(len(sel_tasks)),
            "Tarefas Pendentes": str(pending_count),
        }
        sec_tasks = [
            {
                "header": t.get("title", "Sem título"),
                "detail": f"Status: {t.get('status', 'Pendente')} | Prazo: {t.get('due_date') or 'Sem prazo'}"
            }
            for t in sel_tasks
        ]

        full_pdf = build_pdf_document(
            title="EduTrack AI - Relatorio Academico",
            subtitle=f"Resumo da disciplina {sel_name}",
            metadata=full_meta,
            sections=[{"title": "Listagem de Tarefas Academicas", "items": sec_tasks}]
        )

        st.download_button(
            label="📥 Baixar Relatório em PDF",
            data=full_pdf,
            file_name=f"relatorio_{str(sel_name).lower().replace(' ', '_')}.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True,
        )

# --- TAB 4: CONNECTION DIAGNOSTICS ---
with tab_config:
    st.subheader("⚙️ Diagnóstico de Conexão com o Xano")
    st.caption("Verifique como as URLs e o token estão configurados na sua aplicação.")
    
    config_source = "Streamlit Secrets (.streamlit/secrets.toml)" if hasattr(st, "secrets") and "XANO_BASE_URL" in st.secrets else "Variáveis de Ambiente (.env) / Fallback"
    st.markdown(f"**Origem das Configurações:** `{config_source}`")
    st.markdown(f"**Host Xano:** `{urls['host']}`")
    st.markdown(f"**URL do Grupo de Autenticação:** `{urls['auth']}`")
    st.markdown(f"**URL do Grupo de Disciplinas (Canonical WTDGU8XU):** `{urls['subjects']}`")
    st.markdown(f"**URL do Grupo de Tarefas (Canonical VIQ0W9tI):** `{urls['tasks']}`")
    st.markdown(f"**URL Fallback (Grupo Padrão):** `{urls['fallback_subjects']}`")
    
    st.markdown("---")
    st.markdown("**Status da Sessão:**")
    if user_token:
        st.success("✅ Token JWT presente no `st.session_state`.")
        with st.expander("Visualizar Token (parcial)"):
            st.code(f"{user_token[:30]}...{user_token[-15:]}")
    else:
        st.error("❌ Nenhum token JWT encontrado. Você não está autenticado.")
