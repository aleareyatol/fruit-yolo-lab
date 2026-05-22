import streamlit as st

st.markdown('<h1 style="font-family: monospace; color: #4CAF50;">🍎 Fruit Detection using YOLOv8</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #888;">Artificial Intelligence — Lab 8.0 | Object Detection</p>', unsafe_allow_html=True)
st.markdown("---")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Algorithm", "YOLOv8n")
with col2:
    st.metric("Task", "Object Detection")
with col3:
    st.metric("Dataset Source", "Kaggle")

st.markdown("---")

st.markdown("### What is Object Detection?")
st.info(
    "Object detection is a computer vision task that identifies **what** objects are in an image "
    "and **where** they are located — represented through bounding boxes. Unlike classification, "
    "it can detect multiple objects simultaneously."
)

st.markdown("### What is YOLO?")
st.success(
    "**YOLO (You Only Look Once)** is a real-time object detection algorithm that analyzes the "
    "entire image in a single pass — predicting bounding boxes and class labels simultaneously. "
    "This makes it significantly faster than traditional multi-pass detection methods."
)

st.markdown("### Project Workflow")
steps = [
    ("📦", "Dataset Preparation", "Download fruit detection dataset from Kaggle in YOLO format"),
    ("🏋️", "Model Training", "Fine-tune YOLOv8n pretrained model on the fruit dataset"),
    ("🔍", "Image Testing", "Test the trained model on unseen fruit images"),
    ("📊", "Analysis", "Evaluate performance using Precision, Recall, and mAP"),
]
for icon, title, desc in steps:
    with st.container():
        st.markdown(f"**{icon} {title}** — {desc}")

st.markdown("---")
st.caption("Dataset: Fruit Detection Dataset — Kaggle | Model: YOLOv8n (Ultralytics)")
