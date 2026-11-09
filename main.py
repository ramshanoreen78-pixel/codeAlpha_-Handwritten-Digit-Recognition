 
import streamlit as st
import numpy as np
import cv2
from PIL import Image
import tensorflow as tf

# Page configuration
st.set_page_config(
    page_title="Handwritten Digit Recognition",
    page_icon="✍️",
    layout="centered"
)

# Load trained model only once
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("model.keras")

try:
    model = load_model()
except Exception as e:
    st.error(f"Model loading error: {e}")
    st.stop()

# App heading
st.title("✍️ Handwritten Digit Recognition")
st.write("Upload a handwritten digit image and let AI predict it!")

st.divider()

# Upload image
uploaded_file = st.file_uploader(
    "Upload your digit image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("L")

    st.subheader("Uploaded Image")
    st.image(image, width=200)

    if st.button("Predict Digit"):

        # Image preprocessing
        img = np.array(image)
        img = cv2.resize(img, (28, 28))

        # Invert image if background is white
        if np.mean(img) > 127:
            img = 255 - img

        img = img.astype("float32") / 255.0

        # Prepare input shape
        if len(model.input_shape) == 4:
            img = img.reshape(1, 28, 28, 1)
        else:
            img = img.reshape(1, 784)

        # Prediction
        prediction = model.predict(img)

        predicted_digit = np.argmax(prediction[0])
        confidence = np.max(prediction[0]) * 100

        # Display result
        st.success("Prediction Completed!")

        st.metric("Predicted Digit", predicted_digit)

        st.write(f"Confidence: {confidence:.2f}%")

        st.subheader("Prediction Probabilities")

        st.bar_chart({
            str(i): float(prediction[0][i])
            for i in range(len(prediction[0]))
        })

else:
    st.info("Please upload a handwritten digit image.")


