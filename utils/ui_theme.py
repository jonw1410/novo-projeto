"""
EduTrack AI - UI Theme & Visual Styling Module
Provides modern, vibrant, and harmonic CSS styling for Streamlit.
Eliminates plain white layouts with subtle mesh gradients, vibrant cards,
elevated metric blocks, and lively interactive elements.
"""

import streamlit as st


def apply_custom_theme() -> None:
    """Inject a vibrant, modern, and harmonious CSS theme into the active Streamlit page."""
    custom_css = """
    <style>
    /* ========================================================
       EduTrack AI - Vibrant & Harmonic Visual Theme
       ======================================================== */

    /* Global App Background: Soft ambient mesh gradient (not plain white) */
    .stApp {
        background: radial-gradient(circle at 15% 15%, rgba(99, 102, 241, 0.10) 0%, rgba(248, 250, 252, 0.95) 45%),
                    radial-gradient(circle at 85% 85%, rgba(124, 58, 237, 0.08) 0%, rgba(241, 245, 249, 0.95) 50%),
                    linear-gradient(180deg, #F0F4FF 0%, #F8FAFC 50%, #F1F5F9 100%) !important;
        background-attachment: fixed !important;
    }

    /* Headings: Lively Gradient & Visual Weight */
    h1 {
        background: linear-gradient(120deg, #1E1B4B 0%, #4338CA 50%, #6366F1 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800 !important;
        letter-spacing: -0.02em !important;
        margin-bottom: 0.5rem !important;
    }

    h2, h3 {
        color: #1E293B !important;
        font-weight: 700 !important;
        letter-spacing: -0.01em !important;
    }

    /* Metric Cards: Elevated, Vibrant with Indigo Accent Bar */
    [data-testid="stMetric"] {
        background: #FFFFFF !important;
        border-radius: 14px !important;
        padding: 16px 20px !important;
        box-shadow: 0 4px 20px -2px rgba(79, 70, 229, 0.12), 0 2px 8px -1px rgba(0, 0, 0, 0.04) !important;
        border-left: 5px solid #4F46E5 !important;
        border-top: 1px solid rgba(226, 232, 240, 0.8) !important;
        border-right: 1px solid rgba(226, 232, 240, 0.8) !important;
        border-bottom: 1px solid rgba(226, 232, 240, 0.8) !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }

    [data-testid="stMetric"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 26px -2px rgba(79, 70, 229, 0.22) !important;
    }

    [data-testid="stMetricValue"] {
        color: #4F46E5 !important;
        font-weight: 800 !important;
        font-size: 1.85rem !important;
    }

    [data-testid="stMetricLabel"] {
        color: #475569 !important;
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        text-transform: uppercase !important;
        letter-spacing: 0.6px !important;
    }

    /* Primary & Action Buttons: Rich Vibrant Gradient with Glow Hover */
    button[kind="primary"], 
    .stButton > button[type="primary"], 
    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #4F46E5 0%, #7C3AED 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        padding: 0.55rem 1.4rem !important;
        box-shadow: 0 4px 14px 0 rgba(79, 70, 229, 0.35) !important;
        transition: all 0.2s ease-in-out !important;
    }

    button[kind="primary"]:hover, 
    .stButton > button[type="primary"]:hover, 
    div.stButton > button[kind="primary"]:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 22px 0 rgba(124, 58, 237, 0.50) !important;
        background: linear-gradient(135deg, #4338CA 0%, #6D28D9 100%) !important;
    }

    /* Secondary Buttons: Crisp Slate with Vibrant Border */
    button[kind="secondary"], 
    .stButton > button[type="secondary"] {
        background: #FFFFFF !important;
        color: #334155 !important;
        border: 1.5px solid #CBD5E1 !important;
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease-in-out !important;
    }

    button[kind="secondary"]:hover, 
    .stButton > button[type="secondary"]:hover {
        border-color: #6366F1 !important;
        color: #4F46E5 !important;
        background: #F8FAFC !important;
        box-shadow: 0 2px 10px rgba(99, 102, 241, 0.12) !important;
    }

    /* Download Buttons */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #0284C7 0%, #2563EB 100%) !important;
        color: #FFFFFF !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 14px 0 rgba(2, 132, 199, 0.30) !important;
        transition: all 0.2s ease-in-out !important;
    }

    .stDownloadButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px 0 rgba(37, 99, 235, 0.45) !important;
    }

    /* Tabs Styling: Modern Pills */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px !important;
        background-color: rgba(226, 232, 240, 0.6) !important;
        padding: 6px !important;
        border-radius: 14px !important;
        border: 1px solid rgba(203, 213, 225, 0.6) !important;
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px !important;
        padding: 8px 18px !important;
        font-weight: 600 !important;
        color: #475569 !important;
        border: none !important;
        background-color: transparent !important;
        transition: all 0.2s ease !important;
    }

    .stTabs [aria-selected="true"] {
        background: #FFFFFF !important;
        color: #4F46E5 !important;
        box-shadow: 0 3px 12px rgba(79, 70, 229, 0.18) !important;
    }

    /* Expanders: Card Appearance */
    [data-testid="stExpander"] {
        background: #FFFFFF !important;
        border-radius: 14px !important;
        border: 1px solid #E2E8F0 !important;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03) !important;
        margin-bottom: 14px !important;
        transition: all 0.2s ease !important;
    }

    [data-testid="stExpander"]:hover {
        border-color: #A5B4FC !important;
        box-shadow: 0 4px 16px rgba(79, 70, 229, 0.08) !important;
    }

    /* Alert / Notification Banners */
    .stAlert {
        border-radius: 12px !important;
        font-weight: 500 !important;
        border-width: 1px !important;
        border-style: solid !important;
    }

    /* Input Focus Glow */
    input:focus, select:focus, textarea:focus {
        border-color: #6366F1 !important;
        box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.20) !important;
    }

    /* Sidebar Enhancement: Rich Contrasting Slate */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0F172A 0%, #1E1B4B 100%) !important;
        color: #F8FAFC !important;
    }

    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
    [data-testid="stSidebar"] label {
        color: #E2E8F0 !important;
    }

    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
        background: none !important;
        -webkit-text-fill-color: #FFFFFF !important;
    }

    [data-testid="stSidebarNav"] span {
        color: #E2E8F0 !important;
        font-weight: 600 !important;
    }

    [data-testid="stSidebarNav"] a:hover span {
        color: #818CF8 !important;
    }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
