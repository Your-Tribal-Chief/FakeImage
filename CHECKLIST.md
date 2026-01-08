# ✅ Pre-Training Checklist (Use this on Kaggle/Colab)

## Before Running train.ipynb

### 1. Environment Setup
- [ ] Kaggle/Colab notebook created
- [ ] GPU/TPU enabled (Settings → Accelerator → GPU T4 x2)
- [ ] Internet enabled (for downloading pretrained weights)
- [ ] CIFAKE dataset added/uploaded

### 2. Dataset Verification
- [ ] Dataset has `train` folder
- [ ] Dataset has `test` folder
- [ ] Train folder has `FAKE` and `REAL` subfolders
- [ ] Test folder has `FAKE` and `REAL` subfolders
- [ ] Each subfolder has images

**Run this to verify:**
```python
import os
TRAIN_DIR = '/kaggle/input/cifake-real-and-ai-generated-synthetic-images/train'
print("Classes:", os.listdir(TRAIN_DIR))
# Should print: ['FAKE', 'REAL']
```

### 3. Code Verification
- [ ] train.ipynb uploaded
- [ ] All 13 cells are present
- [ ] Cell 1 is markdown (header)
- [ ] Cells 2-12 are Python code
- [ ] Cell 13 is markdown (summary)

---

## During Training

### Phase 1 (Feature Extraction)
Expected output:
```
✅ Mixed Precision Enabled
✅ Using Default Strategy (GPU/CPU)
📁 Dataset Path: /kaggle/input/...
✅ Train directory found
   Classes: ['FAKE', 'REAL']
🏷️ Class Names: ['FAKE', 'REAL']
   Label 0 → FAKE
   Label 1 → REAL
📊 Training Set Distribution:
   FAKE: 50000 samples (50%)
   REAL: 50000 samples (50%)
⚖️ Class Weights: {0: 1.0, 1: 1.0}
```

**Watch for:**
- [ ] Class names printed correctly
- [ ] No class imbalance warnings
- [ ] Training accuracy improving
- [ ] Validation accuracy improving
- [ ] No NaN losses

### Phase 2 (Fine-Tuning)
Expected output:
```
🔥 PHASE 2: Fine-Tuning EfficientNet Layers
   Trainable layers: 137
```

**Watch for:**
- [ ] Validation accuracy > training accuracy initially (normal!)
- [ ] Learning rate reductions (if needed)
- [ ] Model checkpoint saves
- [ ] No sudden accuracy drops

---

## After Training

### 1. Files Generated
- [ ] `deepfake_detector.keras` exists (check file size ~20-30 MB)
- [ ] `deepfake_detector.h5` exists
- [ ] `label_mapping.txt` exists
- [ ] `training_history.png` generated
- [ ] `confusion_matrix.png` generated
- [ ] `sample_predictions.png` generated

### 2. Performance Verification
Check final output:
```
🎯 Test Results:
   Accuracy:  XX.XX% (should be >95%)
   AUC:       X.XXXX (should be >0.95)
   Precision: X.XXXX (should be >0.90)
   Recall:    X.XXXX (should be >0.90)
```

**Performance Checklist:**
- [ ] Test accuracy > 95%
- [ ] AUC > 0.95
- [ ] Precision > 0.90
- [ ] Recall > 0.90
- [ ] F1-Score > 0.90

### 3. Visual Verification
Check `sample_predictions.png`:
- [ ] Most predictions are correct (green titles)
- [ ] Confidence scores are high (>80%)
- [ ] Images display properly

Check `confusion_matrix.png`:
- [ ] High numbers on diagonal
- [ ] Low numbers off diagonal
- [ ] Both classes have good accuracy

### 4. Label Mapping Verification
Open `label_mapping.txt`:
```
Label 0 (prediction < 0.5): FAKE
Label 1 (prediction > 0.5): REAL
```

- [ ] FAKE is label 0
- [ ] REAL is label 1
- [ ] This matches CIFAKE alphabetical order

---

## Download Checklist

### Required Files (MUST download)
- [ ] `deepfake_detector.keras` (~20-30 MB)
- [ ] `label_mapping.txt` (tiny file)

### Optional Files (Good to have)
- [ ] `training_history.png`
- [ ] `confusion_matrix.png`
- [ ] `sample_predictions.png`
- [ ] `best_model_phase1.keras` (backup)
- [ ] `best_model_phase2.keras` (backup)

---

## Local App Setup Checklist

### 1. File Placement
```bash
cd /Users/sajidhasan/Documents/CSE330/DeepFakeImage
ls -lh
```

Should show:
- [ ] `app.py` (9.4 KB)
- [ ] `deepfake_detector.keras` (20-30 MB) ← Downloaded from Kaggle
- [ ] `label_mapping.txt` ← Downloaded from Kaggle
- [ ] `requirements.txt`
- [ ] `README.md`
- [ ] `RealImage.png` (test image)
- [ ] `FakeImage.png` (test image)

### 2. Dependencies
```bash
pip install -r requirements.txt
```

Check installation:
- [ ] streamlit installed (`streamlit --version`)
- [ ] tensorflow installed (`python -c "import tensorflow as tf; print(tf.__version__)"`)
- [ ] PIL installed (`python -c "from PIL import Image"`)
- [ ] numpy installed (`python -c "import numpy"`)

### 3. Model Loading Test
```bash
python -c "import tensorflow as tf; model = tf.keras.models.load_model('deepfake_detector.keras'); print('✅ Model loaded!')"
```

- [ ] No errors
- [ ] Prints "✅ Model loaded!"

---

## First Run Checklist

### 1. Start the App
```bash
streamlit run app.py
```

Expected output:
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
```

- [ ] No errors during startup
- [ ] Browser opens automatically
- [ ] App loads without errors

### 2. UI Verification
- [ ] Title displays: "🕵️ AI Deepfake Detector"
- [ ] Sidebar appears on left
- [ ] Theme selector works
- [ ] Confidence threshold slider works
- [ ] File uploader appears
- [ ] Welcome screen shows

### 3. Functionality Test

**Test with RealImage.png:**
```
1. Upload RealImage.png
2. Click "Analyze Image"
3. Expected: ✅ REAL IMAGE (green card)
4. Confidence: >70%
```
- [ ] Correctly detects as REAL
- [ ] Green card appears
- [ ] Confidence score shows
- [ ] Metrics display

**Test with FakeImage.png:**
```
1. Upload FakeImage.png
2. Click "Analyze Image"
3. Expected: 🤖 AI-GENERATED (red card)
4. Confidence: >70%
```
- [ ] Correctly detects as FAKE
- [ ] Red card appears
- [ ] Confidence score shows
- [ ] Metrics display

---

## Troubleshooting Checklist

### Issue: Model loading error
- [ ] Check file name: `deepfake_detector.keras` (exact spelling)
- [ ] Check file size: should be 20-30 MB
- [ ] Check TensorFlow version: `pip install --upgrade tensorflow`
- [ ] Try loading in Python REPL to see exact error

### Issue: Still detecting everything as FAKE
- [ ] Verify using NEW trained model (not old one)
- [ ] Check `label_mapping.txt` matches app logic
- [ ] Verify EfficientNet preprocessing is in app.py (line ~90)
- [ ] Test with known real photo (not from dataset)

### Issue: Low accuracy on test images
- [ ] Retrain with more epochs
- [ ] Check data augmentation is enabled
- [ ] Verify GPU was used during training
- [ ] Check class weights were applied

### Issue: App UI looks broken
- [ ] Clear browser cache (Ctrl+Shift+R / Cmd+Shift+R)
- [ ] Try different browser
- [ ] Check streamlit version: `pip install --upgrade streamlit`
- [ ] Restart streamlit server

### Issue: Slow predictions
- [ ] First prediction is always slow (model loading)
- [ ] Subsequent predictions should be fast (<2 sec)
- [ ] Check if using CPU (slower) vs GPU (faster)
- [ ] Check image size (very large images take longer)

---

## Performance Expectations

### Training (Kaggle GPU)
| Metric | Expected |
|--------|----------|
| Phase 1 time | 15-20 min |
| Phase 2 time | 10-15 min |
| Total time | 25-35 min |
| Final accuracy | 95-99% |
| Model size | 20-30 MB |

### Inference (Local)
| Metric | Expected |
|--------|----------|
| First prediction | 3-5 sec |
| Subsequent predictions | 0.5-2 sec |
| CPU inference | 1-3 sec |
| GPU inference | 0.2-1 sec |

---

## Final Verification

Before submitting your project:
- [ ] Model accuracy > 95%
- [ ] App runs without errors
- [ ] UI looks professional
- [ ] Dark mode works
- [ ] Test images work correctly
- [ ] Documentation complete
- [ ] Code is commented
- [ ] Git repo is clean

---

## Success Criteria ✅

Your project is ready when:
1. ✅ Training completes with >95% accuracy
2. ✅ Model file downloads successfully
3. ✅ App starts without errors
4. ✅ Test images are classified correctly
5. ✅ UI looks beautiful (dark mode works)
6. ✅ Confidence scores are reasonable
7. ✅ All documentation files present

---

## Emergency Fixes

### If training fails on Kaggle:
```python
# Reduce batch size
BATCH_SIZE = 16  # Instead of 32

# Reduce epochs
EPOCHS = 10  # Instead of 15
FINE_TUNE_EPOCHS = 5  # Instead of 10
```

### If app crashes:
```python
# Add error handling
try:
    model = tf.keras.models.load_model('deepfake_detector.keras')
except Exception as e:
    st.error(f"Error: {e}")
    st.stop()
```

### If predictions are slow:
```python
# Reduce image size during preprocessing
size = (128, 128)  # Instead of (224, 224)
# Note: This may slightly reduce accuracy
```

---

## Quick Reference

### Training on Kaggle:
```
1. Upload train.ipynb
2. Add CIFAKE dataset
3. Enable GPU
4. Run All
5. Wait 30-45 min
6. Download .keras file
7. Done!
```

### Running App Locally:
```
1. Put .keras file in project folder
2. pip install -r requirements.txt
3. streamlit run app.py
4. Upload test images
5. Done!
```

---

**Print this checklist and follow it step-by-step! 📋✅**

Good luck! 🚀
