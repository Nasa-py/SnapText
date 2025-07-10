import streamlit as st
from PIL import Image
import pytesseract
import pyperclip

# Set Tesseract path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Page config
st.set_page_config(page_title="SnapText", page_icon="🔍", layout="centered")

# Title
st.markdown("<h1 style='text-align: center; color: #6c63ff;'>🔍 SnapText</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>Select an image to extract text instantly</p>", unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"], label_visibility="collapsed")

# If image uploaded
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("🧠 Scanning image..."):
        extracted_text = pytesseract.image_to_string(image)
        pyperclip.copy(extracted_text)

    st.success("✅ Text extracted and copied to clipboard!")
    st.text_area("📋 Extracted Text", value=extracted_text, height=200)

