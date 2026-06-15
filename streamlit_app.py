import streamlit as st
from PIL import Image
import os
import numpy as np

from cnnClassifier.pipeline.predict import PredictionPipeline

# Page configuration
st.set_page_config(
    page_title="Chicken Disease Classification",
    page_icon="🐔",
    layout="centered"
)

st.title("🐔 Chicken Disease Classification")
st.write("Upload a chicken fecal image to predict whether the chicken is healthy or affected by Coccidiosis.")

# Upload image
uploaded_file = st.file_uploader(
    "Choose an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)

    if st.button("Predict"):
        img = image.resize((224,224))
        img = np.array(img)/255.0
        img = np.expand_dims(img, axis=0)

        # Save the uploaded image temporarily
        temp_image_path = "temp_image.jpg"
        image.save(temp_image_path)

        # Pass the temporary image path to the PredictionPipeline
        classifier = PredictionPipeline(temp_image_path)

        result = classifier.predict()

        # Extract the prediction from the result
        prediction = result[0]["image"]

        if prediction == "Healthy":
            st.success("Healthy")
        else:
            st.error("Coccidiosis")

        # Optionally, delete the temporary image file after prediction
        os.remove(temp_image_path)
       