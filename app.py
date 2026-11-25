"""
EduTrack AI - Main Application & Academic Dashboard
Theme: Midnight Navy with Slate Surfaces and Teal Accents
"""

import streamlit as st
import requests
from utils.ui_theme import apply_custom_theme
from utils.xano_client import get_endpoint_urls, request_with_fallback

# Configuração da Página
st.set_page_config(page_title="EduTrack AI - Painel Acadêmico", page_icon="🎓", layout="wide")
apply_custom_theme()

# Header principal
st.markdown("""
<div style="margin-bottom: 1.5rem;">
    <div style="display: inline-flex; align-items: center; gap: 8px; padding: 5px 16px; border-radius: 9999px; background: rgba(71, 201, 176, 0.12); border: 1px solid rgba(103, 211, 197, 0.55); color: #A7F3E9; font-weight: 700; font-size: 0.85rem; letter-spacing: 0.8px; margin-bottom: 10px;">
        <span>🎓</span> AMBIENTE ACADÊMICO INTELIGENTE
    </div>
    <h1 style="margin: 0 0 6px 0;">🎓 EduTrack AI</h1>
    <p style="color: #A9B9CC; font-size: 1.1rem; margin: 0; font-weight: 500;">
        Seu centro integrado de estudos, disciplinas acadêmicas e controle de tarefas em tempo real.
    </p>
</div>
""", unsafe_allow_html=True)

# Sidebar (Menu Lateral)
st.sidebar.header("📌 SELECIONE A OPÇÃO")
menu_option = st.sidebar.radio(
    "Opções",
    ["📊 Dashboard Geral", "📚 Disciplinas", "📝 Tarefas", "👤 Meu Perfil"],
    label_visibility="collapsed"
)

user_token = st.session_state.get("token")
user_profile = st.session_state.get("user") or {}
user_name = user_profile.get("name") or "Estudante"

# Conteúdo Dinâmico
if "Dashboard" in menu_option:
    if user_token:
        st.markdown(f"### 👋 Bem-vindo de volta, **{user_name}**!")
        st.caption("Aqui está o panorama em tempo real da sua jornada acadêmica:")

        # Attempt to load live counts from Xano
        total_subjects = 0
        total_tasks = 0
        completed_tasks = 0
        pending_tasks = 0

        try:
            urls = get_endpoint_urls()
            headers = {"Authorization": f"Bearer {user_token}"}
            s_resp, _ = request_with_fallback("GET", f"{urls['subjects']}/subjects", urls["fallback_subjects"], headers, timeout=5)
            if s_resp.status_code == 200 and isinstance(s_resp.json(), list):
                total_subjects = len(s_resp.json())

            t_resp, _ = request_with_fallback("GET", f"{urls['tasks']}/academic_tasks", urls["fallback_tasks"], headers, timeout=5)
            if t_resp.status_code == 200 and isinstance(t_resp.json(), list):
                tasks_list = t_resp.json()
                total_tasks = len(tasks_list)
                completed_tasks = sum(1 for t in tasks_list if t.get("status") == "Concluída")
                pending_tasks = total_tasks - completed_tasks
        except Exception:
            pass

        pct = int((completed_tasks / total_tasks * 100)) if total_tasks > 0 else 0

        # Metrics Row
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("📚 Disciplinas Ativas", total_subjects)
        c2.metric("⏳ Tarefas Pendentes", pending_tasks)
        c3.metric("✅ Concluídas", completed_tasks)
        c4.metric("📈 Conclusão Geral", f"{pct}%")

        st.progress(pct / 100)
        st.markdown("---")

        st.markdown("#### ⚡ Acesso Rápido aos Módulos de Estudo")
        nav_c1, nav_c2, nav_c3 = st.columns(3)
        with nav_c1:
            st.page_link("pages/1_📚_Disciplinas.py", label="📚 Gerenciar Disciplinas", icon="📖", use_container_width=True)
        with nav_c2:
            st.page_link("pages/2_📝_Tarefas.py", label="📝 Minhas Tarefas", icon="✍️", use_container_width=True)
        with nav_c3:
            st.page_link("pages/3_👤_Perfil.py", label="👤 Detalhes da Conta", icon="👤", use_container_width=True)

    else:
        # Not logged in: welcome hero
        st.markdown("""
        <div style="background: linear-gradient(145deg, #14243A 0%, #101B2D 100%); border: 1px solid rgba(103, 211, 197, 0.28); border-radius: 16px; padding: 24px; margin-bottom: 24px; box-shadow: 0 12px 32px rgba(2, 8, 23, 0.28);">
            <h3 style="color: #A7F3E9; margin-top: 0; font-size: 1.5rem; font-weight: 750;">
                ✨ Bem-vindo ao EduTrack AI!
            </h3>
            <p style="color: #CBD5E1; font-size: 1.05rem; line-height: 1.6;">
                Organize sua vida acadêmica com eficiência máxima. O EduTrack AI sincroniza disciplinas, tarefas e relatórios com banco de dados em nuvem Xano.
            </p>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        col1.metric("📚 Disciplinas Ativas", "—", help="Faça login para ver seus dados reais")
        col2.metric("⏳ Tarefas Pendentes", "—", help="Faça login para ver seus dados reais")
        col3.metric("🎯 Taxa de Conclusão", "—", help="Faça login para ver seus dados reais")

        st.markdown("---")
        st.markdown("#### 🚀 Comece Agora Mesmo:")
        btn_c1, btn_c2, btn_c3 = st.columns(3)
        with btn_c1:
            st.page_link("pages/3_👤_Perfil.py", label="🔐 Entrar / Criar Conta", icon="🚀", use_container_width=True)
        with btn_c2:
            st.page_link("pages/1_📚_Disciplinas.py", label="📚 Explorar Disciplinas", icon="📖", use_container_width=True)
        with btn_c3:
            st.page_link("pages/2_📝_Tarefas.py", label="📝 Explorar Tarefas", icon="✍️", use_container_width=True)

elif "Disciplinas" in menu_option:
    st.subheader("📚 Minhas Disciplinas Acadêmicas")
    st.write("Cadastre e monitore suas disciplinas, professores associados, cargas horárias e emita relatórios em PDF.")
    st.page_link("pages/1_📚_Disciplinas.py", label="👉 Acessar Módulo Completo de Disciplinas", icon="📚", use_container_width=True)

elif "Tarefas" in menu_option:
    st.subheader("📝 Gerenciamento de Tarefas e Atividades")
    st.write("Acompanhe entregas, defina prazos, marque atividades concluídas e exporte resumos acadêmicos completos.")
    st.page_link("pages/2_📝_Tarefas.py", label="👉 Acessar Módulo Completo de Tarefas", icon="📝", use_container_width=True)

elif "Perfil" in menu_option:
    st.subheader("👤 Perfil do Usuário e Autenticação")
    st.write("Gerencie seus dados de acesso, faça login com sua conta Xano ou cadastre-se na plataforma.")
    st.page_link("pages/3_👤_Perfil.py", label="👉 Ir para Tela de Login e Perfil", icon="👤", use_container_width=True)