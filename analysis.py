import streamlit as st
import json
import os

st.markdown('<h1 style="font-family: monospace; color: #4CAF50;">📊 Comparative Analysis</h1>', unsafe_allow_html=True)
st.markdown("---")

# Load saved metrics if available
metrics = None
if os.path.exists("results/metrics.json"):
    with open("results/metrics.json") as f:
        metrics = json.load(f)

if metrics:
    st.markdown("### Your Model Performance")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Precision", f"{metrics['precision']:.3f}")
    col2.metric("Recall", f"{metrics['recall']:.3f}")
    col3.metric("mAP@0.5", f"{metrics['map50']:.3f}")
    col4.metric("mAP@0.5:0.95", f"{metrics['map50_95']:.3f}")
    st.markdown("---")
else:
    st.info("📝 No metrics saved yet. Complete training and save metrics on the Training page.")
    st.markdown("---")

st.markdown("### Lab Q&A — Discussion Questions")

qa = [
    (
        "1. What is object detection?",
        "Object detection is a computer vision task that identifies **what** objects are present "
        "in an image and **where** they are located, represented through bounding boxes with class labels. "
        "Unlike image classification (which gives one label per image), object detection can locate "
        "and label multiple objects within a single image simultaneously."
    ),
    (
        "2. How does YOLO perform object detection?",
        "YOLO (You Only Look Once) divides the input image into a grid and predicts bounding boxes "
        "and class probabilities **simultaneously in a single forward pass** through the neural network. "
        "This makes it much faster than traditional methods that scan the image multiple times. "
        "YOLOv8 further improves accuracy and speed using an anchor-free detection head."
    ),
    (
        "3. What is the role of a pre-annotated dataset?",
        "A pre-annotated dataset provides images that already have **labeled bounding boxes** — "
        "indicating where each object is and what class it belongs to. This allows us to skip manual "
        "labeling and focus directly on model training and evaluation. In this lab, the Kaggle fruit "
        "detection dataset provides ready-to-use annotations in YOLO format."
    ),
    (
        "4. What do Precision, Recall, and mAP measure?",
        "**Precision** measures how many of the model's detected objects were actually correct "
        "(low false positives). **Recall** measures how many actual objects the model successfully "
        "found (low false negatives). **mAP (Mean Average Precision)** combines both into a single "
        "score across all classes and IoU thresholds — it is the standard benchmark for object detection models."
    ),
    (
        "5. What challenges did you encounter during training?",
        "Common challenges include: insufficient training data causing overfitting, imbalanced class "
        "distribution where some fruits appear rarely, high similarity between certain fruits (e.g., "
        "apple vs. orange at a distance), long training time without a GPU, and difficulty detecting "
        "partially occluded or overlapping fruits. These can be mitigated through data augmentation "
        "and increasing training epochs."
    ),
    (
        "6. How can object detection performance be improved?",
        "Performance can be improved by: using a larger dataset with more diverse images, increasing "
        "training epochs, applying data augmentation (flipping, brightness, rotation), using a larger "
        "YOLOv8 variant (yolov8s or yolov8m), tuning hyperparameters like learning rate and batch size, "
        "and ensuring balanced class distribution in the training set."
    ),
]

for question, answer in qa:
    with st.expander(question):
        st.markdown(answer)

st.markdown("---")
st.markdown("### Dataset Reference")
st.markdown("**Dataset used:** Fruit Detection Dataset")
st.link_button("🔗 Kaggle Dataset Link", "https://www.kaggle.com/datasets/lakshaytyagi01/fruit-detection")
st.caption("Include this link in your submission as the dataset source.")
