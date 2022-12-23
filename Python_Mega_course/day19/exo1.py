# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image

st.subheader("Color to Grayscale Converter")

uploaded_image=st.file_uploader("Upload Image")

with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")

if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

if uploaded_image:
    # Create a pillow image instance
    img = Image.open(uploaded_image)

    # Convert it to grayscale
    gray_img = img.convert("L")

    # Render the grayscale image on the webpage
    st.image(gray_img)

