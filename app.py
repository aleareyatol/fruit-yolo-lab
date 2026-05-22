import streamlit as st

st.set_page_config(
    page_title="Fruit Detection Lab",
    page_icon="🍎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar navigation
st.sidebar.markdown("## 🍎 Fruit Detection Lab")
st.sidebar.markdown("*YOLO Object Detection*")
st.sidebar.markdown("---")

pages = {
    "🏠 Overview": "pages/overview.py",
    "📦 Dataset": "pages/dataset.py",
    "🏋️ Training": "pages/training.py",
    "🔍 Detection": "pages/detection.py",
    "📊 Analysis": "pages/analysis.py",
}

page = st.sidebar.radio("Navigate", list(pages.keys()))
st.sidebar.markdown("---")
st.sidebar.caption("Lab 8.0 — Artificial Intelligence")
st.sidebar.caption("Fruit Detection using YOLOv8")

# Route to pages
if page == "🏠 Overview":
    exec(open("pages/overview.py", encoding="utf-8").read())
elif page == "📦 Dataset":
    exec(open("pages/dataset.py", encoding="utf-8").read())
elif page == "🏋️ Training":
    exec(open("pages/training.py", encoding="utf-8").read())
elif page == "🔍 Detection":
    exec(open("pages/detection.py", encoding="utf-8").read())
elif page == "📊 Analysis":
    exec(open("pages/analysis.py", encoding="utf-8").read())
