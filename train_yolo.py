from ultralytics import YOLO

# Load pretrained YOLOv8 nano model
model = YOLO("yolov8n.pt")

# Train on your fruit dataset
results = model.train(
    data="dataset/data.yaml",
    epochs=3,
    imgsz=640,
    name="fruit_detection_run",
    project="runs/detect"
)

print("\n✅ Training complete!")
print(f"Best model saved to: runs/detect/fruit_detection_run/weights/best.pt")

# Evaluate on validation set
print("\n📊 Evaluating model...")
metrics = model.val()

print(f"\nResults:")
print(f"  Precision : {metrics.box.mp:.4f}")
print(f"  Recall    : {metrics.box.mr:.4f}")
print(f"  mAP@0.5   : {metrics.box.map50:.4f}")
print(f"  mAP@0.5:95: {metrics.box.map:.4f}")
