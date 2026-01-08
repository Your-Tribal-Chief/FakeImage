import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np
import time

# ---------------------------------------------------------------------
# 1. Page Config & Custom Styling
# ---------------------------------------------------------------------
st.set_page_config(
    page_title="AI Deepfake Detector",
    page_icon="🕵️",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for beautiful dark/light mode styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        padding: 2rem;
    }
    
    /* Header styling */
    .title-container {
        text-align: center;
        padding: 2rem 0;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .main-title {
        color: white !important;
        font-size: 3rem !important;
        font-weight: 800 !important;
        margin: 0 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .subtitle {
        color: #f0f0f0 !important;
        font-size: 1.2rem !important;
        margin-top: 0.5rem !important;
    }
    
    /* Card styling - Light Mode */
    .info-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        color: #1a202c;
    }
    
    /* Card styling - Dark Mode (Streamlit uses a different approach) */
    @media (prefers-color-scheme: dark) {
        .info-card {
            background: linear-gradient(135deg, #2d3748 0%, #1a202c 100%);
            color: #e2e8f0;
        }
        
        .welcome-text {
            color: #a0aec0 !important;
        }
    }
    
    /* Button styling */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        font-size: 1.2rem !important;
        font-weight: 600 !important;
        padding: 0.75rem 2rem !important;
        border: none !important;
        border-radius: 10px !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
    }
    
    /* File uploader styling */
    .uploadedFile {
        border: 2px dashed #667eea;
        border-radius: 10px;
        padding: 1rem;
    }
    
    /* Result card styling */
    .result-card {
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        text-align: center;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .real-result {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(17, 153, 142, 0.3);
    }
    
    .fake-result {
        background: linear-gradient(135deg, #ee0979 0%, #ff6a00 100%);
        color: white;
        box-shadow: 0 10px 30px rgba(238, 9, 121, 0.3);
    }
    
    /* Progress bar styling */
    .stProgress > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Emoji sizing */
    .big-emoji {
        font-size: 4rem;
        margin: 1rem 0;
    }
    
    /* Improve dark mode readability */
    @media (prefers-color-scheme: dark) {
        .info-card h4 {
            color: #e2e8f0;
        }
        
        .info-card p {
            color: #cbd5e0;
        }
    }
</style>
""", unsafe_allow_html=True)

# Title Section
st.markdown("""
<div class="title-container">
    <h1 class="main-title">🕵️ AI Deepfake Detector</h1>
    <p class="subtitle">Powered by Deep Learning • EfficientNetB0 • CIFAKE Dataset</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------
# 2. Sidebar Configuration
# ---------------------------------------------------------------------
with st.sidebar:
    st.markdown("### ⚙️ Settings")
    
    # Confidence threshold
    confidence_threshold = st.slider(
        "🎯 Confidence Threshold",
        min_value=0.5,
        max_value=0.95,
        value=0.7,
        step=0.05,
        help="Minimum confidence to classify as REAL"
    )
    
    st.markdown("---")
    st.markdown("### 📊 Model Info")
    st.info("""
    **Model:** EfficientNetB0  
    **Dataset:** CIFAKE  
    **Training:** Transfer Learning + Fine-tuning  
    **Input Size:** 224×224 pixels
    """)
    
    st.markdown("---")
    st.markdown("### 📚 How It Works")
    st.markdown("""
    1. Upload an image
    2. AI analyzes pixel patterns
    3. Get instant results
    4. Check confidence score
    """)
    
    st.markdown("---")
    st.markdown("### 💡 Dark Mode")
    st.markdown("""
    **How to enable dark mode:**
    1. Click the **☰** menu (top-right corner)
    2. Click **Settings**
    3. Under **Theme**, select **Dark**
    
    *The app will automatically adjust colors!*
    """)
    
    st.markdown("---")
    st.markdown("### ⚠️ Disclaimer")
    st.warning("No AI detector is 100% accurate. Use as a supplementary tool.")

# ---------------------------------------------------------------------
# 3. Load Model (Cached to run faster)
# ---------------------------------------------------------------------
@st.cache_resource
def load_model():
    try:
        model = tf.keras.models.load_model('deepfake_detector.keras')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

with st.spinner('🔄 Loading AI Model... Please wait...'):
    model = load_model()

if model is None:
    st.error("❌ Failed to load model. Please check if 'deepfake_detector.keras' exists.")
    st.stop()

# ---------------------------------------------------------------------
# 4. Prediction Function with Proper Preprocessing
# ---------------------------------------------------------------------
def import_and_predict(image_data, model):
    """
    Preprocess image and make prediction
    Returns: prediction probability (0 to 1)
    """
    # Resize image to 224x224 (same as training)
    size = (224, 224)
    image = ImageOps.fit(image_data, size, Image.Resampling.LANCZOS)
    
    # Convert to array
    img = np.asarray(image)
    
    # Ensure RGB (3 channels)
    if img.shape[-1] == 4:  # RGBA
        img = img[..., :3]
    elif len(img.shape) == 2:  # Grayscale
        img = np.stack([img] * 3, axis=-1)
    
    # Add batch dimension
    img_reshape = img[np.newaxis, ...]
    
    # Apply EfficientNet preprocessing
    img_preprocessed = tf.keras.applications.efficientnet.preprocess_input(img_reshape)
    
    # Predict
    prediction = model.predict(img_preprocessed, verbose=0)
    
    return prediction[0][0]

# ---------------------------------------------------------------------
# 5. User Interface - File Upload Section
# ---------------------------------------------------------------------
st.markdown("### 📤 Upload Image for Analysis")

# Info cards
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="info-card">
        <h4>✅ Supported Formats</h4>
        <p>JPG, JPEG, PNG</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h4>⚡ Quick Analysis</h4>
        <p>Results in seconds</p>
    </div>
    """, unsafe_allow_html=True)

# File uploader
file = st.file_uploader(
    "Choose an image file",
    type=["jpg", "png", "jpeg"],
    help="Upload an image to check if it's real or AI-generated"
)

if file is not None:
    # Display uploaded image
    image = Image.open(file)
    
    st.markdown("---")
    st.markdown("### 🖼️ Uploaded Image")
    
    # Center the image
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(image, caption='Your Image', use_container_width=True)
    
    # Analysis button
    st.markdown("---")
    if st.button('🔍 Analyze Image', use_container_width=True):
        
        # Progress animation
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        status_text.text("🔄 Preprocessing image...")
        progress_bar.progress(25)
        time.sleep(0.3)
        
        status_text.text("🧠 Running AI analysis...")
        progress_bar.progress(50)
        
        # Make prediction
        confidence = import_and_predict(image, model)
        
        status_text.text("📊 Calculating confidence...")
        progress_bar.progress(75)
        time.sleep(0.3)
        
        status_text.text("✨ Generating results...")
        progress_bar.progress(100)
        time.sleep(0.2)
        
        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()
        
        # Display results
        st.markdown("---")
        st.markdown("### 🎯 Analysis Results")
        
        # CRITICAL FIX: Check label_mapping.txt to verify correct interpretation
        # In CIFAKE dataset, alphabetically: FAKE comes before REAL
        # So: Label 0 = FAKE, Label 1 = REAL
        # Prediction > 0.5 means Label 1 (REAL)
        # Prediction < 0.5 means Label 0 (FAKE)
        
        if confidence > confidence_threshold:
            # REAL IMAGE
            st.markdown(f"""
            <div class="result-card real-result">
                <div class="big-emoji">✅</div>
                <h2 style="margin: 0; font-size: 2.5rem;">AUTHENTIC IMAGE</h2>
                <p style="font-size: 1.3rem; margin-top: 1rem;">This appears to be a REAL photograph</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Confidence meter
            st.markdown("#### 📈 Confidence Score")
            st.progress(float(confidence))
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Real", f"{confidence*100:.1f}%", "High")
            with col2:
                st.metric("Fake", f"{(1-confidence)*100:.1f}%", "Low")
            with col3:
                st.metric("Certainty", f"{abs(confidence-0.5)*200:.1f}%")
            
            st.success("✅ High confidence in authenticity")
            
        else:
            # FAKE IMAGE
            st.markdown(f"""
            <div class="result-card fake-result">
                <div class="big-emoji">🤖</div>
                <h2 style="margin: 0; font-size: 2.5rem;">AI-GENERATED</h2>
                <p style="font-size: 1.3rem; margin-top: 1rem;">This appears to be created by AI</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Confidence meter
            st.markdown("#### 📈 Confidence Score")
            st.progress(float(1 - confidence))
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Fake", f"{(1-confidence)*100:.1f}%", "High")
            with col2:
                st.metric("Real", f"{confidence*100:.1f}%", "Low")
            with col3:
                st.metric("Certainty", f"{abs(confidence-0.5)*200:.1f}%")
            
            st.error("⚠️ High confidence this is AI-generated")
        
        # Additional info
        st.markdown("---")
        st.info("""
        **💡 Understanding the Results:**
        - **Confidence Score:** How certain the AI is about its prediction
        - **Certainty:** Distance from decision boundary (50%)
        - **Threshold:** Adjustable in sidebar (default: 70%)
        
        *Note: Even advanced AI detectors can make mistakes. Use this as one of many tools in your verification process.*
        """)

else:
    # Welcome screen when no file is uploaded
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; padding: 3rem 0;">
        <div style="font-size: 5rem; margin-bottom: 1rem;">🕵️</div>
        <h2>Ready to Detect Deepfakes!</h2>
        <p class="welcome-text" style="font-size: 1.2rem;">Upload an image above to get started</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Feature highlights
    st.markdown("### 🌟 Key Features")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div style="font-size: 3rem;">⚡</div>
            <h4>Lightning Fast</h4>
            <p>Results in seconds with GPU acceleration</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div style="font-size: 3rem;">🎯</div>
            <h4>High Accuracy</h4>
            <p>Trained on thousands of real & AI images</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card" style="text-align: center;">
            <div style="font-size: 3rem;">🔒</div>
            <h4>Privacy First</h4>
            <p>All processing done locally</p>
        </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 1rem 0;">
    <p>🎓 BUET CSE Level-3 Project | Built with ❤️ using Streamlit & TensorFlow</p>
    <p style="font-size: 0.9rem;">Deepfake detection is an ongoing challenge. Always verify critical information through multiple sources.</p>
</div>
""", unsafe_allow_html=True)