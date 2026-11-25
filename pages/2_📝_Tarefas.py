"""
EduTrack AI - Tarefas (Academic Tasks Management)
Full Xano synchronization with JWT authentication, real-time reactive state updates,
smart URL resolution with fallback, detailed diagnostics, and PDF export.
"""

import os
import sys
from datetime import datetime, date
from typing import Any, Dict, List
import requests
import streamlit as st
import pandas as pd
from dotenv import load_dotenv

# Ensure root directory is in sys.path for utils import
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.pdf_generator import build_pdf_document
from utils.xano_client import get_endpoint_urls, parse_xano_error, request_with_fallback, get_config_source_name
from utils.ui_theme import apply_custom_theme

load_dotenv()

st.set_page_config(page_title="Tarefas - EduTrack AI", page_icon="📝", layout="wide")
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
    """Retrieve all subjects for the user to populate dropdowns."""
    headers = {"Authorization": f"Bearer {token}"}
    resp, _ = request_with_fallback("GET", URL_SUBJECTS_PRIMARY, URL_SUBJECTS_FALLBACK, headers)
    resp.raise_for_status()
    data = resp.json()
    return data if isinstance(data, list) else []


def api_get_tasks(token: str) -> List[Dict[str, Any]]:
    """Retrieve all academic tasks belonging to the authenticated user."""
    headers = {"Authorization": f"Bearer {token}"}
    resp, _ = request_with_fallback("GET", URL_TASKS_PRIMARY, URL_TASKS_FALLBACK, headers)
    resp.raise_for_status()
    data = resp.json()
    return data if isinstance(data, list) else []


def api_create_task(
    token: str,
    title: str,
    description: str,
    subject_id: int,
    due_date: str,
    status: str = "Pendente",
) -> Dict[str, Any]:
    """Create a new academic task in Xano."""
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "title": title.strip(),
        "description": description.strip(),
        "subject_id": subject_id,
        "due_date": due_date,
        "status": status,
    }
    resp, _ = request_with_fallback("POST", URL_TASKS_PRIMARY, URL_TASKS_FALLBACK, headers, json_data=payload)
    resp.raise_for_status()
    return resp.json()


def api_update_task_status(token: str, task_id: int, new_status: str) -> Dict[str, Any]:
    """Update task completion status in Xano."""
    headers = {"Authorization": f"Bearer {token}"}
    payload = {"status": new_status}
    url_prim = f"{urls['tasks']}/academic_tasks/{task_id}"
    url_fall = f"{urls['fallback_tasks']}/{task_id}"
    resp, _ = request_with_fallback("PATCH", url_prim, url_fall, headers, json_data=payload)
    resp.raise_for_status()
    return resp.json()


def api_delete_task(token: str, task_id: int) -> bool:
    """Delete an academic task in Xano."""
    headers = {"Authorization": f"Bearer {token}"}
    url_prim = f"{urls['tasks']}/academic_tasks/{task_id}"
    url_fall = f"{urls['fallback_tasks']}/{task_id}"
    resp, _ = request_with_fallback("DELETE", url_prim, url_fall, headers)
    resp.raise_for_status()
    return True


def render_error_diagnostics(exc: requests.RequestException):
    """Render user-friendly error message and technical diagnostics."""
    diag = parse_xano_error(exc)
    st.error(f"❌ **Erro ao conectar com o Xano:** {diag['message']}")
    if diag.get("hint"):
        st.warning(f"💡 **Como resolver:** {diag['hint']}")
        
    with st.expander("🛠️ Detalhes Técnicos da Requisição"):
        st.markdown(f"- **Código HTTP:** `{diag.get('status_code') or 'Sem resposta'}`")
        st.markdown(f"- **URL Primária de Tarefas:** `{URL_TASKS_PRIMARY}`")
        st.markdown(f"- **URL Fallback:** `{URL_TASKS_FALLBACK}`")
        st.markdown(f"- **Token presente na sessão:** `{'Sim (ativo)' if st.session_state.get('token') else 'Não (faça login no Perfil)'}`")


# ------------------------------------------------------------
# Authentication Guard
# ------------------------------------------------------------
user_token = st.session_state.get("token")

st.title("📝 Gestão de Tarefas Acadêmicas")

if not user_token:
    st.warning("🔒 **Acesso restrito:** Você precisa estar autenticado para visualizar e gerenciar suas tarefas.")
    st.info("Por favor, acesse a página de **👤 Perfil** no menu lateral para fazer login ou cadastrar-se.")
    st.stop()

# ------------------------------------------------------------
# Real-Time Data Fetch
# ------------------------------------------------------------
tasks_data: List[Dict[str, Any]] = []
subjects_data: List[Dict[str, Any]] = []
task_error = None

try:
    with st.spinner("Sincronizando tarefas com o Xano..."):
        tasks_data = api_get_tasks(user_token)
        subjects_data = api_get_subjects(user_token)
except requests.RequestException as exc:
    task_error = exc

if task_error:
    render_error_diagnostics(task_error)

# Map subject IDs to names for quick reference
subject_map = {s.get("id"): s.get("name") for s in subjects_data}

# ------------------------------------------------------------
# Page Layout & Tabs
# ------------------------------------------------------------
tab_list, tab_new, tab_export, tab_config = st.tabs([
    "📋 Minhas Tarefas", 
    "➕ Nova Tarefa", 
    "📄 Exportar Relatório em PDF",
    "⚙️ Diagnóstico de Conexão"
])

# --- TAB 1: LIST / MANAGEMENT ---
with tab_list:
    # Summary Metrics
    total_tasks = len(tasks_data)
    completed_tasks = sum(1 for t in tasks_data if t.get("status") == "Concluída")
    pending_tasks = total_tasks - completed_tasks
    progress_pct = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total de Tarefas", total_tasks)
    m2.metric("Pendentes", pending_tasks)
    m3.metric("Concluídas", completed_tasks)
    m4.metric("Taxa de Conclusão", f"{progress_pct}%")

    st.progress(progress_pct / 100)

    st.markdown("---")

    # Filter Controls
    col_search, col_filter, col_subj, col_refresh = st.columns([3, 2, 2, 1])
    with col_search:
        search_query = st.text_input("🔍 Buscar tarefa...", placeholder="Título da tarefa...")
    with col_filter:
        status_filter = st.selectbox("Status", ["Todas", "Pendente", "Concluída"])
    with col_subj:
        subj_filter = st.selectbox("Disciplina", ["Todas"] + [s.get("name") for s in subjects_data])
    with col_refresh:
        st.write("")
        st.write("")
        if st.button("🔄 Atualizar", use_container_width=True):
            st.rerun()

    # Filter data in memory
    filtered_tasks = tasks_data
    if search_query.strip():
        q = search_query.strip().lower()
        filtered_tasks = [t for t in filtered_tasks if q in (t.get("title") or "").lower()]
    if status_filter != "Todas":
        filtered_tasks = [t for t in filtered_tasks if t.get("status") == status_filter]
    if subj_filter != "Todas":
        filtered_tasks = [t for t in filtered_tasks if subject_map.get(t.get("subject_id")) == subj_filter]

    if not filtered_tasks:
        if not task_error:
            st.info("Nenhuma tarefa encontrada para os critérios selecionados.")
    else:
        for task in filtered_tasks:
            t_id = task.get("id")
            t_title = task.get("title") or "Sem título"
            t_description = task.get("description") or "Sem descrição"
            t_status = task.get("status") or "Pendente"
            t_due = task.get("due_date") or "Sem prazo"
            t_subj_name = subject_map.get(task.get("subject_id"), "Sem disciplina")
            is_done = (t_status == "Concluída")

            status_icon = "✅" if is_done else "⏳"
            exp_label = f"{status_icon} **{t_title}** | {t_subj_name} — Prazo: {t_due}"

            with st.expander(exp_label, expanded=not is_done):
                c_details, c_toggle, c_del = st.columns([4, 2, 1])

                with c_details:
                    st.write(f"**Disciplina:** {t_subj_name}")
                    st.write(f"**Descrição:** {t_description}")
                    st.write(f"**Prazo de Entrega:** {t_due}")
                    st.write(f"**Status Atual:** `{t_status}`")
                    st.write(f"**ID no Xano:** `{t_id}`")

                with c_toggle:
                    st.write("")
                    new_val = st.checkbox("Concluída", value=is_done, key=f"chk_task_{t_id}")
                    if new_val != is_done:
                        updated_status = "Concluída" if new_val else "Pendente"
                        try:
                            api_update_task_status(user_token, t_id, updated_status)
                            st.toast(f"Status atualizado para: {updated_status}", icon="🔄")
                            st.rerun()
                        except requests.RequestException as exc:
                            render_error_diagnostics(exc)

                with c_del:
                    st.write("")
                    if st.button("🗑️ Excluir", key=f"btn_del_task_{t_id}", type="secondary", use_container_width=True):
                        try:
                            api_delete_task(user_token, t_id)
                            st.toast(f"Tarefa '{t_title}' excluída!", icon="🗑️")
                            st.rerun()
                        except requests.RequestException as exc:
                            render_error_diagnostics(exc)

# --- TAB 2: CREATE TASK ---
with tab_new:
    st.subheader("Cadastrar Nova Tarefa Acadêmica")
    st.caption("Crie uma nova atividade vinculada a uma das suas disciplinas cadastradas.")

    if not subjects_data:
        st.warning("⚠️ Você precisa ter pelo menos uma disciplina cadastrada para poder criar tarefas.")
        st.info("Acesse a página **📚 Disciplinas** para criar sua primeira matéria.")
    else:
        with st.form("form_create_task", clear_on_submit=True):
            f_title = st.text_input("Título da Tarefa *", placeholder="Ex: Exercícios do Capítulo 3 de Álgebra")
            f_description = st.text_area("Descrição *", placeholder="Descreva os detalhes desta tarefa.")
            
            subject_choices = {s.get("name"): s.get("id") for s in subjects_data}
            f_subject_name = st.selectbox("Disciplina Associada *", list(subject_choices.keys()))
            
            f_due_date = st.date_input("Data de Entrega / Prazo", value=date.today())
            f_status = st.selectbox("Status Inicial", ["Pendente", "Concluída"])

            submitted_task = st.form_submit_button("💾 Salvar Tarefa", type="primary")

            if submitted_task:
                if not f_title.strip():
                    st.warning("Por favor, preencha o título da tarefa.")
                elif not f_description.strip():
                    st.warning("Por favor, preencha a descrição da tarefa.")
                else:
                    selected_subj_id = subject_choices[f_subject_name]
                    due_date_str = f_due_date.strftime("%Y-%m-%d")
                    try:
                        with st.spinner("Salvando tarefa no Xano..."):
                            api_create_task(
                                token=user_token,
                                title=f_title,
                                description=f_description,
                                subject_id=selected_subj_id,
                                due_date=due_date_str,
                                status=f_status,
                            )
                            st.success(f"✅ Tarefa '{f_title}' cadastrada com sucesso no Xano!")
                            st.rerun()
                    except requests.RequestException as exc:
                        render_error_diagnostics(exc)

# --- TAB 3: PDF EXPORT ---
with tab_export:
    st.subheader("📄 Exportar Listagem de Tarefas em PDF")
    st.caption("Gere um relatório completo com todas as suas tarefas acadêmicas organizadas por disciplina.")

    if not tasks_data:
        st.info("Nenhuma tarefa para exportar.")
    else:
        # Group tasks by subject
        sections_for_pdf = []
        for s in subjects_data:
            s_id = s.get("id")
            s_name = s.get("name")
            s_tasks = [t for t in tasks_data if t.get("subject_id") == s_id]
            if s_tasks:
                items = [
                    {
                        "header": t.get("title", "Sem título"),
                        "detail": f"Status: {t.get('status', 'Pendente')} | Prazo: {t.get('due_date') or 'Sem prazo'}"
                    }
                    for t in s_tasks
                ]
                sections_for_pdf.append({
                    "title": f"Disciplina: {s_name} ({len(s_tasks)} tarefas)",
                    "items": items
                })

        # Add unassociated tasks if any
        orphan_tasks = [t for t in tasks_data if not t.get("subject_id") or t.get("subject_id") not in subject_map]
        if orphan_tasks:
            sections_for_pdf.append({
                "title": "Outras Atividades",
                "items": [
                    {
                        "header": t.get("title", "Sem título"),
                        "detail": f"Status: {t.get('status', 'Pendente')} | Prazo: {t.get('due_date') or 'Sem prazo'}"
                    }
                    for t in orphan_tasks
                ]
            })

        tasks_meta = {
            "Total de Tarefas": str(total_tasks),
            "Tarefas Concluidas": str(completed_tasks),
            "Tarefas Pendentes": str(pending_tasks),
            "Taxa de Conclusao": f"{progress_pct}%",
        }

        tasks_pdf = build_pdf_document(
            title="EduTrack AI - Listagem de Tarefas",
            subtitle="Relatorio Geral de Atividades Academicas",
            metadata=tasks_meta,
            sections=sections_for_pdf
        )

        st.download_button(
            label="📥 Baixar Relatório Completo de Tarefas (PDF)",
            data=tasks_pdf,
            file_name="edutrack_tarefas_academicas.pdf",
            mime="application/pdf",
            type="primary",
            use_container_width=True,
        )

# --- TAB 4: CONNECTION DIAGNOSTICS ---
with tab_config:
    st.subheader("⚙️ Diagnóstico de Conexão com o Xano")
    st.caption("Verifique como as URLs e o token estão configurados na sua aplicação.")
    
    config_source = get_config_source_name()
    st.markdown(f"**Origem das Configurações:** `{config_source}`")
    st.markdown(f"**Host Xano:** `{urls['host']}`")
    st.markdown(f"**URL do Grupo de Tarefas (Canonical VIQ0W9tI):** `{urls['tasks']}`")
    st.markdown(f"**URL do Grupo de Disciplinas (Canonical WTDGU8XU):** `{urls['subjects']}`")
    st.markdown(f"**URL Fallback (Grupo Padrão):** `{urls['fallback_tasks']}`")
    
    st.markdown("---")
    st.markdown("**Status da Sessão:**")
    if user_token:
        st.success("✅ Token JWT presente no `st.session_state`.")
        with st.expander("Visualizar Token (parcial)"):
            st.code(f"{user_token[:30]}...{user_token[-15:]}")
    else:
        st.error("❌ Nenhum token JWT encontrado. Você não está autenticado.")
