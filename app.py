import streamlit as st
import streamlit.components.v1 as components
import os

# Configuração da Página para tela cheia e moderna (chamada única no início do script)
st.set_page_config(
    page_title="EduTrack AI - Portal Acadêmico",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estilização para remover margens excessivas do Streamlit e garantir imersão total
st.markdown("""
<style>
    .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 0.5rem;
        padding-right: 0.5rem;
        max-width: 100%;
    }
    header[data-testid="stHeader"] {
        display: none;
    }
    footer {
        display: none;
    }
</style>
""", unsafe_allow_html=True)

# Caminho do dashboard moderno
html_file = os.path.join(os.path.dirname(__file__), "dashboard.html")

if os.path.exists(html_file):
    with open(html_file, "r", encoding="utf-8") as f:
        html_code = f.read()
    
    # Renderiza o dashboard HTML moderno, responsivo e interativo
    components.html(html_code, height=1350, scrolling=True)
else:
    st.title("🎓 EduTrack AI")
    st.error("Arquivo dashboard.html não encontrado no diretório do projeto.")
