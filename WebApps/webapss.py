import streamlit as st
import pickle
import cv2
import numpy as np
from PIL import Image
from sklearn.preprocessing import LabelEncoder
from utils import preprocess_image, extract_features

# Muat model dari file pickle
with open('cancer_model_new.pkl', 'rb') as f:
    data = pickle.load(f)

models = data['models']
class_names = data['class_names']
le = data['label_encoder']

# Fungsi untuk memprediksi gambar
def predict(image):
    img = np.array(image)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    img = preprocess_image(img)
    
    features = extract_features(img)
    features = np.array(features).reshape(1, -1)
    
    predictions = {}
    for name, model in models.items():
        pred = model.predict(features)
        pred_class = class_names[pred[0]]
        proba = model.predict_proba(features)[0]
        predictions[name] = {
            'class': pred_class,
            'probability': max(proba)
        }
    
    return predictions

# Antarmuka Streamlit
st.title('Klasifikasi Kanker Paru-paru')

uploaded_file = st.file_uploader("Unggah gambar CT Scan paru-paru", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Gambar yang diunggah', use_column_width=True)
    
    if st.button('Prediksi'):
        predictions = predict(image)
        
        st.subheader('Hasil Prediksi:')
        for model_name, pred in predictions.items():
            st.write(f"**{model_name}**:")
            st.write(f"- Kelas: {pred['class']}")
            st.write(f"- Probabilitas: {pred['probability']:.2f}")
            st.progress(pred['probability'])
            st.write("---")