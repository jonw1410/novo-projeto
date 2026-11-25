"""
EduTrack AI - UI Theme & Visual Styling Module
Theme: "Midnight Navy, Slate & Teal"
Fundo principal e lateral em azul-marinho, superfícies em ardósia e destaques teal.
"""

import base64
import streamlit as st

_WAVE_LINES_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="100%" height="100%" preserveAspectRatio="none">
  <defs>
    <linearGradient id="wave1" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FDE047" stop-opacity="0.0"/>
      <stop offset="25%" stop-color="#FDE047" stop-opacity="0.25"/>
      <stop offset="70%" stop-color="#FEF08A" stop-opacity="0.30"/>
      <stop offset="100%" stop-color="#EAB308" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="wave2" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.0"/>
      <stop offset="30%" stop-color="#FEF9C3" stop-opacity="0.20"/>
      <stop offset="70%" stop-color="#FDE047" stop-opacity="0.24"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0.0"/>
    </linearGradient>
    <linearGradient id="wave3" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#F59E0B" stop-opacity="0.0"/>
      <stop offset="35%" stop-color="#FEF08A" stop-opacity="0.22"/>
      <stop offset="75%" stop-color="#FDE047" stop-opacity="0.26"/>
      <stop offset="100%" stop-color="#F59E0B" stop-opacity="0.0"/>
    </linearGradient>
  </defs>
  <!-- Ondas em Linha Superiores -->
  <path d="M-100,140 C320,40 640,220 1050,110 C1460,0 1720,160 2020,100" fill="none" stroke="url(#wave1)" stroke-width="2"/>
  <path d="M-100,190 C340,90 660,270 1070,160 C1480,50 1740,210 2020,150" fill="none" stroke="url(#wave2)" stroke-width="1.8"/>
  <path d="M-100,240 C360,140 680,320 1090,210 C1500,100 1760,260 2020,200" fill="none" stroke="url(#wave1)" stroke-width="1.4" stroke-dasharray="10 6"/>
  <path d="M-100,290 C380,190 700,370 1110,260 C1520,150 1780,310 2020,250" fill="none" stroke="url(#wave3)" stroke-width="1.6"/>
  <path d="M-100,340 C400,240 720,420 1130,310 C1540,200 1800,360 2020,300" fill="none" stroke="url(#wave2)" stroke-width="1.2"/>
  <path d="M-100,390 C420,290 740,470 1150,360 C1560,250 1820,410 2020,350" fill="none" stroke="url(#wave1)" stroke-width="1.0" stroke-dasharray="6 8"/>

  <!-- Ondas em Linha Inferiores -->
  <path d="M-100,660 C300,500 720,820 1180,640 C1540,500 1780,700 2020,620" fill="none" stroke="url(#wave2)" stroke-width="2"/>
  <path d="M-100,710 C320,550 740,870 1200,690 C1560,550 1800,750 2020,670" fill="none" stroke="url(#wave1)" stroke-width="1.8"/>
  <path d="M-100,760 C340,600 760,920 1220,740 C1580,600 1820,800 2020,720" fill="none" stroke="url(#wave3)" stroke-width="1.4" stroke-dasharray="12 6"/>
  <path d="M-100,810 C360,650 780,970 1240,790 C1600,650 1840,850 2020,770" fill="none" stroke="url(#wave2)" stroke-width="1.6"/>
  <path d="M-100,860 C380,700 800,1020 1260,840 C1620,700 1860,900 2020,820" fill="none" stroke="url(#wave1)" stroke-width="1.2"/>
  <path d="M-100,910 C400,750 820,1070 1280,890 C1640,750 1880,950 2020,870" fill="none" stroke="url(#wave3)" stroke-width="1.0" stroke-dasharray="8 6"/>
</svg>"""

_WAVE_LINES_B64 = base64.b64encode(_WAVE_LINES_SVG.encode("utf-8")).decode("utf-8")


def get_study_background_b64() -> str:
    """Retained for backward compatibility; returns empty string."""
    return ""


def apply_custom_theme() -> None:
    """Apply the EduTrack midnight navy and teal theme to the active Streamlit page."""
    custom_css = """
    <style>
    /* ========================================================
       EduTrack AI - Royal Sapphire & Midnight Navy Theme
       ======================================================== */

    /* Ondas em Linha Douradas e Celestiais no Fundo */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-image: url("data:image/svg+xml;base64,__WAVE_LINES_B64__");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        pointer-events: none;
        z-index: 0;
        opacity: 0.85;
    }

    /* Global Background: Harmonia Perfeita com a Lateral #0B1F3A (Deep Midnight Navy) */
    .stApp {
        background-color: #0D1B32 !important;
        background-image:
            radial-gradient(circle at 18% 15%, rgba(253, 224, 71, 0.08) 0%, transparent 45%),
            radial-gradient(circle at 82% 22%, rgba(56, 189, 248, 0.10) 0%, transparent 45%),
            radial-gradient(circle at 50% 85%, rgba(11, 31, 58, 0.40) 0%, transparent 55%),
            linear-gradient(180deg, #0A1629 0%, #0D1B32 50%, #10223E 100%) !important;
        background-attachment: fixed !important;
        color: #F8FAFC !important;
    }

    .main .block-container {
        position: relative;
        z-index: 1;
    }

    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* General typography contrast on dark canvas */
    .stApp p, .stApp span, .stApp label, .stApp div {
        color: #E2E8F0;
    }

    /* Headings: Blazing Golden Fire (Intense, Radiant & Fiery) */
    h1 {
        background: linear-gradient(125deg, #FFFFFF 0%, #FEF08A 25%, #F59E0B 65%, #EA580C 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 900 !important;
        letter-spacing: -0.02em !important;
        filter: drop-shadow(0 0 18px rgba(245, 158, 11, 0.55));
        margin-bottom: 0.6rem !important;
    }

    h2, h3 {
        color: #FDE047 !important;
        font-weight: 800 !important;
        letter-spacing: -0.01em !important;
        text-shadow: 0 0 12px rgba(245, 158, 11, 0.4);
    }

    h4, h5, h6 {
        color: #FCD34D !important;
        font-weight: 700 !important;
    }

    /* Metric Cards: Dark Obsidian with Fiery Gold Left Bar & Amber Aura */
    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #15151D 0%, #0E0E14 100%) !important;
        border-radius: 14px !important;
        padding: 18px 22px !important;
        box-shadow: 0 4px 26px -2px rgba(245, 158, 11, 0.28), 0 2px 12px -1px rgba(0, 0, 0, 0.8) !important;
        border-left: 5px solid #F59E0B !important;
        border-top: 1px solid rgba(245, 158, 11, 0.4) !important;
        border-right: 1px solid rgba(245, 158, 11, 0.25) !important;
        border-bottom: 1px solid rgba(245, 158, 11, 0.25) !important;
        transition: transform 0.25s ease, box-shadow 0.25s ease, border-color 0.25s ease !important;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-3px) scale(1.01) !important;
        box-shadow: 0 8px 36px 0 rgba(245, 158, 11, 0.50), 0 0 20px rgba(234, 88, 12, 0.35) !important;
        border-color: #FBBF24 !important;
    }

    [data-testid="stMetricValue"] {
        background: linear-gradient(135deg, #FFFFFF 0%, #FEF08A 25%, #F59E0B 75%, #EA580C 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 900 !important;
        font-size: 2.2rem !important;
        filter: drop-shadow(0 0 12px rgba(245, 158, 11, 0.45));
    }

    [data-testid="stMetricLabel"] {
        color: #FDE047 !important;
        font-weight: 800 !important;
        font-size: 0.85rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.9px !important;
    }

    /* Primary Buttons & Botão Entrar: Dourado Elegante, Limpo & Profissional */
    button[kind="primary"], 
    .stButton > button[type="primary"], 
    div.stButton > button[kind="primary"],
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(180deg, #FBBF24 0%, #F59E0B 100%) !important;
        color: #0A0E1A !important;
        font-weight: 800 !important;
        font-size: 1.05rem !important;
        border: 1px solid #D97706 !important;
        border-radius: 10px !important;
        padding: 0.65rem 1.8rem !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.28), 0 1px 2px rgba(0, 0, 0, 0.16) !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
        text-shadow: none !important;
    }

    button[kind="primary"]:hover, 
    .stButton > button[type="primary"]:hover, 
    div.stButton > button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-1px) scale(1.01) !important;
        background: linear-gradient(180deg, #FCD34D 0%, #F59E0B 100%) !important;
        color: #000000 !important;
        border-color: #F59E0B !important;
        box-shadow: 0 4px 14px rgba(245, 158, 11, 0.35), 0 2px 4px rgba(0, 0, 0, 0.2) !important;
    }

    /* Secondary Buttons: Dark Obsidian with Glowing Golden Outline */
    button[kind="secondary"], 
    .stButton > button[type="secondary"] {
        background: rgba(20, 20, 28, 0.9) !important;
        color: #FDE047 !important;
        border: 1.5px solid #F59E0B !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
        box-shadow: 0 2px 12px rgba(245, 158, 11, 0.2) !important;
        transition: all 0.2s ease-in-out !important;
    }

    button[kind="secondary"]:hover, 
    .stButton > button[type="secondary"]:hover {
        border-color: #FBBF24 !important;
        color: #FFFFFF !important;
        background: rgba(245, 158, 11, 0.25) !important;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.5) !important;
        transform: translateY(-1px) !important;
    }

    /* Download / Export Buttons: Golden Fire Burst */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #DC2626 0%, #EA580C 40%, #F59E0B 80%, #FDE047 100%) !important;
        color: #0A0A0E !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 22px 0 rgba(245, 158, 11, 0.50) !important;
        transition: all 0.2s ease-in-out !important;
        text-transform: uppercase !important;
        letter-spacing: 0.5px !important;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 30px 0 rgba(245, 158, 11, 0.80), 0 0 20px rgba(253, 224, 71, 0.6) !important;
        color: #000000 !important;
    }

    /* Tabs Styling: Dark with Fiery Gold Active Pill */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px !important;
        background-color: rgba(14, 14, 20, 0.95) !important;
        padding: 8px !important;
        border-radius: 16px !important;
        border: 2px solid rgba(245, 158, 11, 0.45) !important;
        box-shadow: 0 6px 24px rgba(0, 0, 0, 0.7), 0 0 18px rgba(245, 158, 11, 0.2) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 12px !important;
        padding: 12px 28px !important;
        font-weight: 800 !important;
        font-size: 1.15rem !important;
        color: #94A3B8 !important;
        border: none !important;
        background-color: transparent !important;
        transition: all 0.25s ease !important;
        letter-spacing: 0.4px !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #FDE047 !important;
        background: rgba(245, 158, 11, 0.15) !important;
        transform: translateY(-1px) !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.42) 0%, rgba(234, 88, 12, 0.32) 100%) !important;
        color: #FEF08A !important;
        border: 2px solid #F59E0B !important;
        box-shadow: 0 0 24px rgba(245, 158, 11, 0.55), inset 0 0 10px rgba(245, 158, 11, 0.2) !important;
        font-weight: 900 !important;
    }

    /* Forms (Login, Cadastro & formulários destacados) */
    [data-testid="stForm"] {
        background: linear-gradient(180deg, rgba(16, 16, 24, 0.98) 0%, rgba(10, 10, 16, 0.98) 100%) !important;
        border: 2px solid rgba(245, 158, 11, 0.45) !important;
        border-radius: 20px !important;
        padding: 2.2rem 2.5rem !important;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.85), 0 0 28px rgba(245, 158, 11, 0.22) !important;
    }

    [data-testid="stForm"] label,
    .stTextInput label {
        font-size: 1.08rem !important;
        font-weight: 800 !important;
        color: #FDE047 !important;
        letter-spacing: 0.3px !important;
        margin-bottom: 6px !important;
    }

    [data-testid="stForm"] button[kind="primary"],
    [data-testid="stForm"] .stButton > button,
    [data-testid="stFormSubmitButton"] > button {
        background: linear-gradient(180deg, #FBBF24 0%, #F59E0B 100%) !important;
        color: #0A0E1A !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        padding: 0.85rem 2.2rem !important;
        border-radius: 12px !important;
        border: 1px solid #D97706 !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.35), 0 2px 4px rgba(0, 0, 0, 0.2) !important;
        letter-spacing: 0.6px !important;
        margin-top: 1rem !important;
        text-shadow: none !important;
    }

    [data-testid="stForm"] button[kind="primary"]:hover,
    [data-testid="stForm"] .stButton > button:hover,
    [data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-1px) scale(1.01) !important;
        box-shadow: 0 6px 18px rgba(245, 158, 11, 0.40), 0 2px 6px rgba(0, 0, 0, 0.25) !important;
        background: linear-gradient(180deg, #FCD34D 0%, #F59E0B 100%) !important;
        color: #000000 !important;
        border-color: #F59E0B !important;
    }

    /* Expanders: Dark Obsidian with Fiery Gold Edges */
    [data-testid="stExpander"] {
        background: rgba(18, 18, 25, 0.95) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(245, 158, 11, 0.35) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.6) !important;
        margin-bottom: 14px !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stExpander"]:hover {
        border-color: #F59E0B !important;
        box-shadow: 0 4px 25px rgba(245, 158, 11, 0.25) !important;
    }

    /* Alert / Notification Banners */
    .stAlert {
        border-radius: 12px !important;
        font-weight: 600 !important;
        border: 1px solid rgba(245, 158, 11, 0.5) !important;
        background: rgba(22, 19, 14, 0.95) !important;
    }

    /* Inputs: Dark Base with Glowing Gold Focus & Higher Padding */
    .stTextInput > div > div > input, 
    .stNumberInput > div > div > input, 
    .stSelectbox > div > div, 
    textarea {
        background-color: #08080C !important;
        color: #FFFFFF !important;
        border: 1.8px solid rgba(245, 158, 11, 0.45) !important;
        border-radius: 12px !important;
        padding: 12px 16px !important;
        font-size: 1.1rem !important;
        min-height: 48px !important;
        transition: all 0.2s ease !important;
    }

    .stTextInput > div > div > input:focus, 
    .stNumberInput > div > div > input:focus, 
    textarea:focus {
        border-color: #FBBF24 !important;
        background-color: #0E0E16 !important;
        box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.40), 0 0 20px rgba(245, 158, 11, 0.35) !important;
    }

    /* Dataframe & Tables: Dark Obsidian with Gold Frame */
    [data-testid="stDataFrame"] {
        background: #0E0E14 !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7) !important;
    }

    /* ========================================================
       Sidebar: Cor #0B1F3A, Botões #1C1C1E e Destaque Dourado
       ======================================================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #071528 0%, #0B1F3A 50%, #061222 100%) !important;
        background-color: #0B1F3A !important;
        border-right: 2px solid rgba(253, 224, 71, 0.45) !important;
        box-shadow: 4px 0 28px rgba(7, 21, 39, 0.85) !important;
    }

    [data-testid="stSidebar"] * {
        color: #FDE047 !important;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        background: linear-gradient(135deg, #FFFFFF 0%, #FEF9C3 20%, #FDE047 60%, #F59E0B 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-size: 1.35rem !important;
        font-weight: 900 !important;
        letter-spacing: 0.8px !important;
        filter: drop-shadow(0 0 16px rgba(253, 224, 71, 0.60));
        margin-bottom: 1.2rem !important;
    }

    /* Links de Navegação nativos na Barra Lateral (Streamlit Pages) */
    [data-testid="stSidebarNav"] {
        padding-top: 0.5rem !important;
        padding-bottom: 0.5rem !important;
    }

    [data-testid="stSidebarNav"] a {
        background: #1C1C1E !important;
        background-color: #1C1C1E !important;
        border: 1.5px solid rgba(253, 224, 71, 0.40) !important;
        border-radius: 12px !important;
        margin: 8px 0 !important;
        padding: 12px 16px !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        display: flex !important;
        align-items: center !important;
        gap: 12px !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.45) !important;
    }

    [data-testid="stSidebarNav"] a:hover {
        background: #2C2C2E !important;
        background-color: #2C2C2E !important;
        border-color: #FDE047 !important;
        box-shadow: 0 0 22px rgba(253, 224, 71, 0.45) !important;
        transform: translateX(4px) scale(1.02) !important;
    }

    [data-testid="stSidebarNav"] span {
        color: #FDE047 !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.4px !important;
        text-shadow: 0 0 10px rgba(253, 224, 71, 0.45) !important;
    }

    [data-testid="stSidebarNav"] svg {
        width: 1.45rem !important;
        height: 1.45rem !important;
        color: #FDE047 !important;
        filter: drop-shadow(0 0 8px rgba(253, 224, 71, 0.6)) !important;
    }

    [data-testid="stSidebarNav"] a:hover span {
        color: #FFFFFF !important;
        text-shadow: 0 0 14px rgba(253, 224, 71, 0.95) !important;
    }

    [data-testid="stSidebarNav"] a:hover svg {
        color: #FEF9C3 !important;
        filter: drop-shadow(0 0 12px rgba(253, 224, 71, 0.95)) !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, rgba(253, 224, 71, 0.30) 0%, #1C1C1E 100%) !important;
        border: 2px solid #FDE047 !important;
        border-left: 6px solid #FDE047 !important;
        box-shadow: 0 0 26px rgba(253, 224, 71, 0.55), inset 0 0 10px rgba(253, 224, 71, 0.20) !important;
        transform: translateX(2px) !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #FFFFFF !important;
        font-size: 1.18rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 14px rgba(253, 224, 71, 0.95) !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] svg {
        color: #FFFFFF !important;
        filter: drop-shadow(0 0 12px rgba(253, 224, 71, 1.0)) !important;
    }

    /* Radio buttons de navegação na Sidebar (Dashboard / app.py) */
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background: #1C1C1E !important;
        background-color: #1C1C1E !important;
        border-radius: 12px !important;
        padding: 12px 18px !important;
        margin-bottom: 10px !important;
        border: 1.5px solid rgba(253, 224, 71, 0.40) !important;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
        cursor: pointer !important;
        display: flex !important;
        align-items: center !important;
        box-shadow: 0 4px 14px rgba(0, 0, 0, 0.45) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: #2C2C2E !important;
        background-color: #2C2C2E !important;
        border-color: #FDE047 !important;
        box-shadow: 0 0 20px rgba(253, 224, 71, 0.45) !important;
        transform: translateX(4px) scale(1.02) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label span {
        color: #FDE047 !important;
        font-size: 1.15rem !important;
        font-weight: 800 !important;
        letter-spacing: 0.4px !important;
        text-shadow: 0 0 10px rgba(253, 224, 71, 0.45) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover span {
        color: #FFFFFF !important;
        text-shadow: 0 0 14px rgba(253, 224, 71, 0.95) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(135deg, rgba(253, 224, 71, 0.30) 0%, #1C1C1E 100%) !important;
        border: 2px solid #FDE047 !important;
        border-left: 6px solid #FDE047 !important;
        box-shadow: 0 0 26px rgba(253, 224, 71, 0.55), inset 0 0 10px rgba(253, 224, 71, 0.20) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] span {
        color: #FFFFFF !important;
        font-size: 1.18rem !important;
        font-weight: 900 !important;
        text-shadow: 0 0 14px rgba(253, 224, 71, 0.95) !important;
    }

    /* Unified EduTrack palette: midnight navy, slate surfaces, and restrained teal. */
    .stApp {
        background-color: #0B1220 !important;
        background-image:
            radial-gradient(circle at 16% 12%, rgba(71, 201, 176, 0.07) 0%, transparent 42%),
            radial-gradient(circle at 84% 24%, rgba(56, 189, 248, 0.06) 0%, transparent 44%),
            linear-gradient(180deg, #0A1423 0%, #0B1220 58%, #0D1929 100%) !important;
        color: #E6EDF7 !important;
    }

    .stApp::before {
        opacity: 0.2;
    }

    .stApp p, .stApp span, .stApp label, .stApp div {
        color: #D7E1EC;
    }

    h1 {
        background: linear-gradient(120deg, #F8FAFC 0%, #C8E7E3 62%, #67D3C5 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        filter: none !important;
        font-weight: 800 !important;
    }

    h2, h3, h4, h5, h6 {
        color: #A7F3E9 !important;
        text-shadow: none !important;
    }

    [data-testid="stMetric"] {
        background: linear-gradient(145deg, #14243A 0%, #101B2D 100%) !important;
        border: 1px solid #263B52 !important;
        border-left: 4px solid #47C9B0 !important;
        border-radius: 14px !important;
        box-shadow: 0 8px 24px rgba(2, 8, 23, 0.25) !important;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-2px) !important;
        border-color: #397B79 !important;
        box-shadow: 0 12px 28px rgba(2, 8, 23, 0.34) !important;
    }

    [data-testid="stMetricValue"] {
        color: #F1F5F9 !important;
        background: none !important;
        -webkit-text-fill-color: #F1F5F9 !important;
        filter: none !important;
    }

    [data-testid="stMetricLabel"] {
        color: #A9B9CC !important;
    }

    button[kind="primary"],
    .stButton > button[type="primary"],
    div.stButton > button[kind="primary"],
    [data-testid="stFormSubmitButton"] > button {
        background: #0F766E !important;
        color: #FFFFFF !important;
        border: 1px solid #16877D !important;
        box-shadow: 0 4px 12px rgba(2, 8, 23, 0.24) !important;
        text-transform: none !important;
    }

    button[kind="primary"]:hover,
    .stButton > button[type="primary"]:hover,
    div.stButton > button[kind="primary"]:hover,
    [data-testid="stFormSubmitButton"] > button:hover {
        background: #0D9488 !important;
        border-color: #2CB6A5 !important;
        box-shadow: 0 6px 16px rgba(15, 118, 110, 0.24) !important;
    }

    button[kind="secondary"],
    .stButton > button[type="secondary"] {
        background: #14243A !important;
        color: #CDECE9 !important;
        border: 1px solid #345166 !important;
        box-shadow: none !important;
    }

    button[kind="secondary"]:hover,
    .stButton > button[type="secondary"]:hover {
        background: #1A3048 !important;
        border-color: #47C9B0 !important;
        color: #F1F5F9 !important;
        box-shadow: 0 4px 14px rgba(2, 8, 23, 0.22) !important;
    }

    .stDownloadButton > button {
        background: #0F766E !important;
        color: #FFFFFF !important;
        box-shadow: 0 4px 14px rgba(2, 8, 23, 0.25) !important;
        text-transform: none !important;
    }

    .stDownloadButton > button:hover {
        background: #0D9488 !important;
        box-shadow: 0 6px 18px rgba(15, 118, 110, 0.24) !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        gap: 6px !important;
        background: #101B2D !important;
        border: 1px solid #263B52 !important;
        box-shadow: none !important;
        border-radius: 12px !important;
    }

    .stTabs [data-baseweb="tab"] {
        color: #A9B9CC !important;
    }

    .stTabs [data-baseweb="tab"]:hover,
    .stTabs [aria-selected="true"] {
        background: #19333F !important;
        color: #A7F3E9 !important;
        border: 1px solid #397B79 !important;
        box-shadow: none !important;
    }

    [data-testid="stForm"] {
        background: linear-gradient(160deg, #14243A 0%, #101B2D 100%) !important;
        border: 1px solid #2B4258 !important;
        border-radius: 16px !important;
        box-shadow: 0 12px 32px rgba(2, 8, 23, 0.3) !important;
    }

    [data-testid="stForm"] label,
    .stTextInput label {
        color: #B8DCD8 !important;
    }

    [data-testid="stExpander"] {
        background: #111C2E !important;
        border: 1px solid #293F55 !important;
        box-shadow: 0 4px 16px rgba(2, 8, 23, 0.2) !important;
    }

    [data-testid="stExpander"]:hover {
        border-color: #397B79 !important;
        box-shadow: 0 6px 18px rgba(2, 8, 23, 0.24) !important;
    }

    .stAlert {
        background: #14243A !important;
        border: 1px solid #345166 !important;
        border-radius: 12px !important;
    }

    .stTextInput > div > div > input,
    .stNumberInput > div > div > input,
    .stSelectbox > div > div,
    textarea {
        background-color: #0D1929 !important;
        color: #E6EDF7 !important;
        border: 1px solid #345166 !important;
        border-radius: 10px !important;
    }

    .stTextInput > div > div > input:focus,
    .stNumberInput > div > div > input:focus,
    textarea:focus {
        border-color: #47C9B0 !important;
        box-shadow: 0 0 0 2px rgba(71, 201, 176, 0.2) !important;
    }

    [data-testid="stDataFrame"] {
        background: #111C2E !important;
        border: 1px solid #293F55 !important;
        box-shadow: none !important;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0E1A2B 0%, #101D30 100%) !important;
        border-right: 1px solid #263B52 !important;
        box-shadow: 4px 0 20px rgba(2, 8, 23, 0.2) !important;
    }

    [data-testid="stSidebar"] * {
        color: #D7E1EC !important;
    }

    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3 {
        color: #A7F3E9 !important;
        background: none !important;
        -webkit-text-fill-color: #A7F3E9 !important;
        filter: none !important;
    }

    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background: #14243A !important;
        border: 1px solid #263B52 !important;
        border-radius: 10px !important;
        box-shadow: none !important;
    }

    [data-testid="stSidebarNav"] a:hover,
    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: #1A3048 !important;
        border-color: #397B79 !important;
        box-shadow: 0 4px 14px rgba(2, 8, 23, 0.22) !important;
        transform: translateX(2px) !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"],
    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background: #19333F !important;
        border-color: #47C9B0 !important;
        border-left: 3px solid #47C9B0 !important;
        box-shadow: none !important;
    }

    [data-testid="stSidebarNav"] span,
    [data-testid="stSidebarNav"] svg,
    [data-testid="stSidebar"] div[role="radiogroup"] label span {
        color: #CDECE9 !important;
        text-shadow: none !important;
        filter: none !important;
    }
    </style>
    """
    st.markdown(custom_css.replace("__WAVE_LINES_B64__", _WAVE_LINES_B64), unsafe_allow_html=True)
