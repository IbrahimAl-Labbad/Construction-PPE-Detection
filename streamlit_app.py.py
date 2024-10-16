import streamlit as st
import requests
from PIL import Image
from io import BytesIO

# FastAPI endpoint URL
FASTAPI_URL = "http://127.0.0.1:8001/detect"

# Set the title and layout of the Streamlit page
st.set_page_config(page_title="Construction PPE Detection", layout="wide")
st.title("Construction PPE Detection")

# File uploader for image input
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Ensure the uploaded file is in bytes format
    files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
    
    response = requests.post(FASTAPI_URL, files=files)

    if response.status_code == 200:
        # Display the processed image
        image = Image.open(BytesIO(response.content))
        st.image(image, caption="Detected Objects", use_column_width=True)
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
