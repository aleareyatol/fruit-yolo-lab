import streamlit as st
import os

st.markdown('<h1 style="font-family: monospace; color: #4CAF50;">📦 Dataset Preparation</h1>', unsafe_allow_html=True)
st.markdown("---")

st.markdown("### Step 1 — Download the Dataset")
st.markdown(
    "Use the **Fruit Detection Dataset** from Kaggle. It is already formatted for YOLO "
    "with train/val/test splits."
)

st.link_button(
    "🔗 Open Dataset on Kaggle",
    "https://www.kaggle.com/datasets/lakshaytyagi01/fruit-detection"
)

st.markdown("---")
st.markdown("### Step 2 — Expected Folder Structure")
st.code("""
fruit_yolo_lab/
├── app.py
├── pages/
├── dataset/
│   ├── data.yaml
│   ├── train/
│   │   ├── images/
│   │   └── labels/
│   ├── valid/
│   │   ├── images/
│   │   └── labels/
│   └── test/
│       ├── images/
│       └── labels/
""", language="bash")

st.markdown("### Step 3 — Check Your data.yaml")
st.markdown("Your `data.yaml` should look like this:")
st.code("""
train: train/images
val: valid/images
test: test/images

nc: 6
names: ['apple', 'banana', 'grape', 'mango', 'orange', 'strawberry']
""", language="yaml")

st.markdown("---")
st.markdown("### Step 4 — Verify Dataset")

dataset_path = st.text_input("Enter your dataset path", value="dataset")

if st.button("✅ Check Dataset"):
    yaml_path = os.path.join(dataset_path, "data.yaml")
    train_path = os.path.join(dataset_path, "train", "images")
    val_path = os.path.join(dataset_path, "valid", "images")
    test_path = os.path.join(dataset_path, "test", "images")

    checks = {
        "data.yaml found": os.path.exists(yaml_path),
        "train/images found": os.path.exists(train_path),
        "valid/images found": os.path.exists(val_path),
        "test/images found": os.path.exists(test_path),
    }

    all_ok = True
    for label, ok in checks.items():
        if ok:
            st.success(f"✅ {label}")
        else:
            st.error(f"❌ {label}")
            all_ok = False

    if all_ok:
        train_imgs = len(os.listdir(train_path))
        val_imgs = len(os.listdir(val_path))
        test_imgs = len(os.listdir(test_path))
        st.info(f"📊 Images — Train: {train_imgs} | Val: {val_imgs} | Test: {test_imgs}")
        st.balloons()
