import streamlit as st
import os
import json

st.markdown('<h1 style="font-family: monospace; color: #4CAF50;">🏋️ Model Training</h1>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("### Training Configuration")

col1, col2, col3 = st.columns(3)
with col1:
    epochs = st.number_input("Epochs", min_value=5, max_value=100, value=20)
with col2:
    imgsz = st.selectbox("Image Size", [416, 640, 832], index=1)
with col3:
    model_size = st.selectbox("YOLOv8 Model", ["yolov8n.pt", "yolov8s.pt", "yolov8m.pt"], index=0)

data_yaml = st.text_input("Path to data.yaml", value="dataset/data.yaml")

st.markdown("---")
st.markdown("### Generated Training Code")
st.code(f"""
from ultralytics import YOLO

# Load pretrained YOLOv8 model
model = YOLO("{model_size}")

# Train on fruit dataset
results = model.train(
    data="{data_yaml}",
    epochs={epochs},
    imgsz={imgsz},
    name="fruit_detection_run",
    project="runs/detect"
)

print("Training complete!")
""", language="python")

st.info("💡 Copy this code and run it in your terminal or Jupyter notebook.")

st.markdown("---")
st.markdown("### Run Training via Terminal")
st.code(f"""
# Install ultralytics first
pip install ultralytics

# Then run training
python train_yolo.py
""", language="bash")

st.markdown("---")
st.markdown("### Training Results")
st.markdown("After training, upload your `results.png` from the runs folder:")

results_img = st.file_uploader("Upload results.png (training curves)", type=["png", "jpg"])
if results_img:
    st.image(results_img, caption="Training Results", use_container_width=True)

st.markdown("### Paste Your Metrics")
st.markdown("After running `model.val()`, paste the output below:")

metrics_col1, metrics_col2 = st.columns(2)
with metrics_col1:
    precision = st.number_input("Precision", 0.0, 1.0, 0.0, step=0.001, format="%.3f")
    recall = st.number_input("Recall", 0.0, 1.0, 0.0, step=0.001, format="%.3f")
with metrics_col2:
    map50 = st.number_input("mAP@0.5", 0.0, 1.0, 0.0, step=0.001, format="%.3f")
    map50_95 = st.number_input("mAP@0.5:0.95", 0.0, 1.0, 0.0, step=0.001, format="%.3f")

if st.button("💾 Save Metrics"):
    metrics = {
        "precision": precision,
        "recall": recall,
        "map50": map50,
        "map50_95": map50_95
    }
    os.makedirs("results", exist_ok=True)
    with open("results/metrics.json", "w") as f:
        json.dump(metrics, f)
    st.success("✅ Metrics saved! Go to the Analysis page to view them.")
