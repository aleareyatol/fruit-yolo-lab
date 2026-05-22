# 🍎 Fruit Detection Lab — YOLOv8
**Lab 8.0 | Artificial Intelligence**

---

## Setup Instructions

### 1. Install dependencies
```bash
pip install ultralytics streamlit pillow
```

### 2. Download the dataset
- Go to: https://www.kaggle.com/datasets/lakshaytyagi01/fruit-detection
- Download and extract into a `dataset/` folder inside this project
- Make sure `dataset/data.yaml` exists

### 3. Train the model
```bash
python train_yolo.py
```
This saves the best model to `runs/detect/fruit_detection_run/weights/best.pt`

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

## Project Structure
```
fruit_yolo_lab/
├── app.py                  # Main Streamlit app
├── train_yolo.py           # Training script
├── requirements.txt
├── pages/
│   ├── overview.py         # Project overview
│   ├── dataset.py          # Dataset verification
│   ├── training.py         # Training config & results
│   ├── detection.py        # Live detection on uploaded images
│   └── analysis.py         # Q&A + metrics dashboard
└── dataset/
    ├── data.yaml
    ├── train/images/ & labels/
    ├── valid/images/ & labels/
    └── test/images/ & labels/
```

---

## Submission Checklist
- [ ] Source code (this folder)
- [ ] Screenshots of training results (results.png)
- [ ] Screenshots of detection outputs
- [ ] Recorded performance metrics (Precision, Recall, mAP)
- [ ] Short discussion/analysis (see Analysis page)
- [ ] Dataset link: https://www.kaggle.com/datasets/lakshaytyagi01/fruit-detection

**Deadline: May 25, 2026**
