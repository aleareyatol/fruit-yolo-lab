import streamlit as st
import os
import tempfile
from PIL import Image

st.markdown('<h1 style="font-family: monospace; color: #4CAF50;">🔍 Test & Detect</h1>', unsafe_allow_html=True)
st.markdown('<p style="color: #888;">Run your trained model on new images and visualize detections.</p>', unsafe_allow_html=True)
st.markdown("---")

# Model selection
st.markdown("### Step 1 — Select Model")
model_path = st.text_input(
    "Path to trained model weights (.pt file)",
    value=st.session_state.get('model_path', 'best.pt'),
    help="Use best.pt from your training run, or yolov8n.pt for a demo with COCO classes"
)
st.session_state['model_path'] = model_path

confidence = st.slider("Confidence Threshold", 0.1, 1.0, 0.25, 0.05)

st.markdown("---")
st.markdown("### Step 2 — Upload Test Image")

uploaded_file = st.file_uploader("Choose a fruit image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🚀 Run Detection"):
        if False:
            st.error(f"❌ Model not found at: `{model_path}`")
            st.info("Please train your model first or check the path.")
        else:
            with st.spinner("Running YOLO detection..."):
                try:
                    from ultralytics import YOLO
                    import numpy as np

                    model = YOLO(model_path)

                    # Save uploaded image temporarily
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
                        image.save(tmp.name)
                        tmp_path = tmp.name

                    results = model.predict(
                        source=tmp_path,
                        conf=confidence,
                        save=True,
                        project="runs/detect",
                        name="streamlit_test"
                    )

                    result = results[0]
                    annotated = result.plot()
                    annotated_img = Image.fromarray(annotated[..., ::-1])

                    st.markdown("### Detection Result")
                    st.image(annotated_img, caption="Detected Objects", use_container_width=True)

                    # Show detection summary
                    boxes = result.boxes
                    if len(boxes) == 0:
                        st.warning("No objects detected. Try lowering the confidence threshold.")
                    else:
                        st.markdown(f"**{len(boxes)} object(s) detected:**")
                        names = model.names
                        for i, box in enumerate(boxes):
                            cls = int(box.cls[0])
                            conf_score = float(box.conf[0])
                            label = names[cls]
                            coords = box.xyxy[0].tolist()
                            st.markdown(
                                f"- **{label}** — Confidence: `{conf_score:.2%}` | "
                                f"Box: `[{int(coords[0])}, {int(coords[1])}, {int(coords[2])}, {int(coords[3])}]`"
                            )

                    os.unlink(tmp_path)

                except ImportError:
                    st.error("❌ Ultralytics not installed. Run: `pip install ultralytics`")
                except Exception as e:
                    st.error(f"❌ Detection error: {str(e)}")

st.markdown("---")
st.markdown("### No model yet? Try a Quick Demo")
st.info(
    "You can test with `yolov8n.pt` (pretrained on COCO classes like apple, orange) "
    "by setting the model path to just `yolov8n.pt`. It will auto-download."
)
