"""
EduTrack AI - UI Theme & Visual Styling Module
Theme: "Dark Golden Fire" (Escuro Dourado Fogo)
Combines deep luxury obsidian dark with glowing molten gold and fierce fire flame accents.
"""

import streamlit as st


def apply_custom_theme() -> None:
    """Inject the Dark Golden Fire theme into the active Streamlit page."""
    custom_css = """
    <style>
    /* ========================================================
       EduTrack AI - Dark Golden Fire Theme
       (Tema Escuro - Dourado Fogo Intenso)
       ======================================================== */

    /* Global Background: Deep Obsidian Dark with Molten Gold & Fire Aura */
    .stApp {
        background: radial-gradient(circle at 12% 15%, rgba(245, 158, 11, 0.20) 0%, transparent 45%),
                    radial-gradient(circle at 88% 18%, rgba(234, 88, 12, 0.18) 0%, transparent 45%),
                    radial-gradient(circle at 50% 85%, rgba(217, 119, 6, 0.15) 0%, transparent 55%),
                    linear-gradient(180deg, #09090D 0%, #111117 50%, #0C0C10 100%) !important;
        background-attachment: fixed !important;
        color: #F8FAFC !important;
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

    /* Primary Buttons: Pure Fiery Gold (Molten Blaze & Burning Flame) */
    button[kind="primary"], 
    .stButton > button[type="primary"], 
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #B91C1C 0%, #DC2626 25%, #EA580C 65%, #F59E0B 100%) !important;
        color: #FFFFFF !important;
        font-weight: 900 !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.6rem 1.6rem !important;
        box-shadow: 0 4px 22px 0 rgba(245, 158, 11, 0.60), 0 0 14px rgba(234, 88, 12, 0.40) !important;
        transition: all 0.25s ease-in-out !important;
        text-transform: uppercase !important;
        letter-spacing: 0.6px !important;
    }

    button[kind="primary"]:hover, 
    .stButton > button[type="primary"]:hover, 
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 6px 32px 0 rgba(245, 158, 11, 0.85), 0 0 25px rgba(251, 191, 36, 0.7) !important;
        background: linear-gradient(135deg, #991B1B 0%, #B91C1C 25%, #DC2626 60%, #EA580C 100%) !important;
        color: #FFFFFF !important;
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
        gap: 8px !important;
        background-color: rgba(18, 18, 26, 0.95) !important;
        padding: 6px !important;
        border-radius: 14px !important;
        border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.6) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px !important;
        padding: 8px 18px !important;
        font-weight: 700 !important;
        color: #94A3B8 !important;
        border: none !important;
        background-color: transparent !important;
        transition: all 0.2s ease !important;
    }

    .stTabs [data-baseweb="tab"]:hover {
        color: #FDE047 !important;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.35) 0%, rgba(234, 88, 12, 0.28) 100%) !important;
        color: #FEF08A !important;
        border: 1.5px solid #F59E0B !important;
        box-shadow: 0 0 18px rgba(245, 158, 11, 0.40) !important;
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

    /* Inputs: Dark Base with Glowing Gold Focus */
    .stTextInput > div > div > input, 
    .stNumberInput > div > div > input, 
    .stSelectbox > div > div, 
    textarea {
        background-color: #0E0E14 !important;
        color: #F8FAFC !important;
        border: 1.5px solid rgba(245, 158, 11, 0.4) !important;
        border-radius: 10px !important;
        transition: all 0.2s ease !important;
    }

    .stTextInput > div > div > input:focus, 
    .stNumberInput > div > div > input:focus, 
    textarea:focus {
        border-color: #F59E0B !important;
        box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.35), 0 0 15px rgba(245, 158, 11, 0.25) !important;
    }

    /* Dataframe & Tables: Dark Obsidian with Gold Frame */
    [data-testid="stDataFrame"] {
        background: #0E0E14 !important;
        border-radius: 12px !important;
        border: 1.5px solid rgba(245, 158, 11, 0.35) !important;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.7) !important;
    }

    /* ========================================================
       Sidebar: Dark Obsidian with Glowing Fiery Gold
       ======================================================== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #07070A 0%, #101017 50%, #16120C 100%) !important;
        border-right: 2px solid #F59E0B !important;
        box-shadow: 4px 0 26px rgba(245, 158, 11, 0.30) !important;
    }

    [data-testid="stSidebar"] * {
        color: #E2E8F0 !important;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        background: linear-gradient(135deg, #FFFFFF 0%, #FDE047 30%, #F59E0B 70%, #EA580C 100%) !important;
        -webkit-background-clip: text !important;
        -webkit-text-fill-color: transparent !important;
        font-weight: 900 !important;
        filter: drop-shadow(0 0 12px rgba(245, 158, 11, 0.5));
    }

    /* Links de Navegação na Barra Lateral */
    [data-testid="stSidebarNav"] a {
        background: rgba(18, 18, 26, 0.85) !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
        border-radius: 10px !important;
        margin: 5px 0 !important;
        padding: 8px 12px !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebarNav"] a:hover {
        background: rgba(245, 158, 11, 0.2) !important;
        border-color: #FBBF24 !important;
        box-shadow: 0 0 16px rgba(245, 158, 11, 0.4) !important;
        transform: translateX(3px) !important;
    }

    [data-testid="stSidebarNav"] span {
        color: #E2E8F0 !important;
        font-weight: 700 !important;
    }

    [data-testid="stSidebarNav"] a:hover span {
        color: #FEF08A !important;
        text-shadow: 0 0 10px rgba(251, 191, 36, 0.7) !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.30) 0%, rgba(234, 88, 12, 0.22) 100%) !important;
        border: 1.5px solid #F59E0B !important;
        border-left: 5px solid #F59E0B !important;
        box-shadow: 0 0 20px rgba(245, 158, 11, 0.45) !important;
    }

    [data-testid="stSidebarNav"] a[aria-current="page"] span {
        color: #FEF08A !important;
        font-weight: 900 !important;
        text-shadow: 0 0 8px rgba(251, 191, 36, 0.6) !important;
    }

    /* Radio buttons de navegação na Sidebar (Dashboard / app.py) */
    [data-testid="stSidebar"] div[role="radiogroup"] label {
        background: rgba(18, 18, 26, 0.85) !important;
        border-radius: 10px !important;
        padding: 8px 14px !important;
        margin-bottom: 6px !important;
        border: 1px solid rgba(245, 158, 11, 0.3) !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label:hover {
        background: rgba(245, 158, 11, 0.2) !important;
        border-color: #FBBF24 !important;
        box-shadow: 0 0 14px rgba(245, 158, 11, 0.35) !important;
        transform: translateX(2px) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label span {
        color: #E2E8F0 !important;
        font-weight: 700 !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(135deg, rgba(245, 158, 11, 0.35) 0%, rgba(234, 88, 12, 0.25) 100%) !important;
        border: 1.5px solid #F59E0B !important;
        border-left: 5px solid #F59E0B !important;
        box-shadow: 0 0 18px rgba(245, 158, 11, 0.45) !important;
    }

    [data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] span {
        color: #FEF08A !important;
        font-weight: 900 !important;
        text-shadow: 0 0 8px rgba(251, 191, 36, 0.6) !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
