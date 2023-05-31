import streamlit as st
import tensorflow as tf
from efficientnet.tfkeras import EfficientNetB3
from tensorflow.keras.models import load_model
import numpy as np
import tensorflow.keras.utils as image

st.set_page_config(layout="wide")

st.markdown("<h1 style='text-align: center;'>Free-Predict</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>🎍Predict Ornamental Plant🎍 </h3>", unsafe_allow_html=True)
st.text("")
st.divider()
col1, col2 = st.columns(2)

class_names = ['Agglonema', 'Alocasia', 'Gelombang Cinta', 'Janda Bolong', 'Lidah Mertua', 'Lili Paris', 'Pucuk Merah', 'Suplir']

with st.spinner('Compiling & Load the model..'):
    model = load_model('Saved_Models/model_EfficientNetB3.h5',compile=False)
    model.compile(optimizer = 'adam', 
                loss = 'categorical_crossentropy', 
                metrics = ['accuracy'])

with col1:
    uploaded_files = st.file_uploader("Choose a file", type=['png', 'jpg','jpeg'])
    if uploaded_files is not None:
        bytes_data = uploaded_files.getvalue()
        st.image(bytes_data)

        with st.spinner('Predicting...'):
            img = image.load_img(uploaded_files, target_size=(200,200))
            x = image.img_to_array(img)
            x = x/255.0
            x = np.expand_dims(x, axis=0)
            images = np.vstack([x])

            pred = model.predict(images)
            

with col2:
    if uploaded_files is not None:
        predict_list = np.round(pred,3)
        for i,j in enumerate(predict_list[0]):
            st.text(class_names[i])
            st.progress(float(j), text=f'{str(np.round(j,2))}%')