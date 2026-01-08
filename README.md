# 🕵️ AI Deepfake Image Detector

**BUET CSE Level-3 Project**

A high-accuracy deepfake detection system using Transfer Learning with EfficientNetB0 and the CIFAKE dataset.

---

## 🎯 What Was Fixed

### Training Code Issues ✅
1. **Proper Cell Structure**: Converted single plaintext cell to multiple organized Python cells
2. **Data Augmentation**: Added comprehensive augmentation pipeline (critical for 99%+ accuracy)
3. **Better Architecture**: Added BatchNormalization and improved classification head
4. **Class Weight Balancing**: Handles imbalanced datasets automatically
5. **Label Verification**: Prints class mapping to avoid prediction errors
6. **EfficientNet Preprocessing**: Uses proper `preprocess_input` function
7. **Enhanced Training**: 2-phase training (feature extraction + fine-tuning)
8. **Better Callbacks**: ModelCheckpoint, EarlyStopping, ReduceLROnPlateau
9. **Visualization**: Confusion matrix and sample predictions for verification
10. **Memory Efficient**: Optimized for Kaggle/Colab free tier

### App.py Issues ✅
1. **Beautiful UI**: Modern gradient design with smooth animations
2. **Dark Mode Support**: CSS styling that works with both themes
3. **Proper Preprocessing**: Added EfficientNet preprocessing (THIS WAS THE MAIN BUG!)
4. **RGB Conversion**: Handles RGBA and grayscale images correctly
5. **Better UX**: Progress bars, loading animations, clear results
6. **Confidence Threshold**: Adjustable in sidebar (default 70%)
7. **Sidebar Features**: Model info, settings, how it works guide
8. **Error Handling**: Graceful model loading with error messages
9. **Result Visualization**: Beautiful cards with confidence metrics
10. **Privacy Note**: Disclaimer about AI accuracy

---

## 🚀 Quick Start

### 1. Train the Model (On Kaggle/Colab)

```bash
# Upload train.ipynb to Kaggle
# Select Dataset: CIFAKE - Real and AI-Generated Synthetic Images
# Enable GPU/TPU accelerator
# Run all cells
```

**Expected Results:**
- Training Time: ~30-45 minutes (with GPU)
- Test Accuracy: 95-99%+
- Files Generated:
  - `deepfake_detector.keras` (main model)
  - `label_mapping.txt` (verify label order)
  - `training_history.png` (training curves)
  - `confusion_matrix.png` (performance)

### 2. Download Model Files

```bash
# From Kaggle output, download:
# - deepfake_detector.keras
# - label_mapping.txt (check this!)
```

### 3. Run the Streamlit App

```bash
# Install dependencies
pip install streamlit tensorflow pillow numpy

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🔑 Key Improvements for 99%+ Accuracy

### 1. Data Augmentation ⭐⭐⭐
```python
# Random flips, rotations, zoom, contrast, brightness
# Prevents overfitting and improves generalization
```

### 2. Proper Preprocessing ⭐⭐⭐
```python
# EfficientNet requires specific preprocessing
tf.keras.applications.efficientnet.preprocess_input(img)
```

### 3. Class Weight Balancing ⭐⭐
```python
# Handles imbalanced datasets
# Prevents bias toward majority class
```

### 4. Two-Phase Training ⭐⭐
```python
# Phase 1: Train classification head (frozen base)
# Phase 2: Fine-tune top layers (low learning rate)
```

### 5. Better Architecture ⭐
```python
# Added BatchNormalization for stability
# Deeper classification head (256 -> 128 -> 1)
# Proper dropout rates
```

---

## 📊 Understanding Label Mapping

**CRITICAL:** The CIFAKE dataset has alphabetically ordered labels:
- `FAKE` → Label 0
- `REAL` → Label 1

**Prediction Logic:**
```python
if prediction > 0.5:
    result = "REAL"  # Model predicts label 1
else:
    result = "FAKE"  # Model predicts label 0
```

**Always check `label_mapping.txt` after training!**

---

## 🎨 UI Features

### Dark Mode Support
- Auto-detects system theme
- Beautiful gradient backgrounds
- Smooth animations

### Interactive Elements
- Adjustable confidence threshold
- Real-time progress bars
- Detailed confidence metrics
- Sidebar with model info

### Result Display
- ✅ Green card for REAL images
- 🤖 Red card for FAKE images
- Confidence breakdown
- Certainty percentage

---

## 📈 Expected Performance

| Metric | Expected Value |
|--------|---------------|
| Accuracy | 95-99%+ |
| AUC | 0.98-0.99+ |
| Precision | 94-98% |
| Recall | 94-98% |
| Training Time | 30-45 min (GPU) |

---

## 🐛 Common Issues & Solutions

### Issue: App detects all images as FAKE
**Solution:** 
1. Check `label_mapping.txt` from training
2. Ensure proper preprocessing in app.py
3. Retrain model with fixed code

### Issue: Low accuracy (~50%)
**Solution:**
1. Enable data augmentation
2. Train for more epochs
3. Check class imbalance
4. Verify dataset is loaded correctly

### Issue: Out of memory on Kaggle
**Solution:**
1. Reduce BATCH_SIZE to 16
2. Use mixed precision (already enabled)
3. Don't use .cache() (already removed)

### Issue: Model not loading in app
**Solution:**
1. Check file path: `deepfake_detector.keras`
2. Ensure model file is in same directory as app.py
3. Try loading with full path

---

## 🔧 Customization

### Adjust Confidence Threshold
```python
# In sidebar, default is 0.7 (70%)
# Lower = more sensitive to fakes
# Higher = more strict on calling real
```

### Change Batch Size
```python
# In train.ipynb, cell 3
BATCH_SIZE = 32  # Reduce if OOM
```

### Modify Epochs
```python
# In train.ipynb, cell 3
EPOCHS = 15          # Initial training
FINE_TUNE_EPOCHS = 10  # Fine-tuning
```

---

## 📚 Tech Stack

- **Framework:** TensorFlow 2.x / Keras
- **Model:** EfficientNetB0 (ImageNet pre-trained)
- **Dataset:** CIFAKE (120,000 images)
- **UI:** Streamlit
- **Training:** Kaggle / Google Colab

---

## 🎓 Learning Resources

- [EfficientNet Paper](https://arxiv.org/abs/1905.11946)
- [Transfer Learning Guide](https://www.tensorflow.org/tutorials/images/transfer_learning)
- [CIFAKE Dataset](https://www.kaggle.com/datasets/birdy654/cifake-real-and-ai-generated-synthetic-images)

---

## ⚠️ Limitations

1. **Not 100% Accurate**: AI detection is an ongoing research problem
2. **Dataset Specific**: Trained on CIFAKE (32x32 upscaled images)
3. **Adversarial Attacks**: May be fooled by specifically crafted images
4. **Evolving AI**: New generation models may bypass detection
5. **Context Needed**: Should be used alongside other verification methods

---

## 📝 Notes for Kaggle/Colab

### Kaggle Setup
```python
# Dataset path auto-detection works
# Just ensure CIFAKE dataset is added to notebook
# Enable GPU/TPU in settings
```

### Google Colab Setup
```python
# Upload dataset to Google Drive
# Update DATASET_PATH in cell 3
# Enable GPU: Runtime > Change runtime type > GPU
```

### Free Tier Limits
- ✅ Batch size: 32 works fine
- ✅ Mixed precision: Speeds up training
- ✅ No .cache(): Prevents RAM crashes
- ✅ Prefetch: Optimizes data loading

---

## 🤝 Contributing

This is a university project, but suggestions are welcome!

---

## 📄 License

Educational Project - BUET CSE Level-3

---

## 🙏 Acknowledgments

- CIFAKE Dataset creators
- TensorFlow/Keras team
- Streamlit team
- EfficientNet authors

---

## 📞 Support

If you encounter issues:
1. Check `label_mapping.txt` matches app logic
2. Verify model preprocessing
3. Review training logs for errors
4. Ensure dataset is loaded correctly

---

**Built with ❤️ by BUET CSE Students**

*Deepfake detection is a challenging problem. This tool should be used as a supplementary verification method, not as the sole source of truth.*
