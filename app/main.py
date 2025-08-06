# app/main.py

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from app.controller import AgentController

# Setup Streamlit page
st.set_page_config(page_title="TransfuSense", layout="wide")
st.title("🧠 TransfuSense AI Agent")

# Initialize agent controller
controller = AgentController()

# Sidebar: Choose a tool
tool = st.sidebar.radio(
    "Choose a Tool",
    ["Translator", "Summarizer", "FAQ Bot", "Transfusion Predictor", "OCR Reader", "Full Pipeline"]
)

# Input fields
user_input = st.text_input("Enter your query or upload file:")
uploaded_file = st.file_uploader("Upload Image or CSV File", type=["png", "jpg", "jpeg", "csv"])

# Handle button
if st.button("Run Tool"):

    # Prepare input for the agent
    prompt = ""

    if tool == "Translator":
        prompt = f"translate the report: {user_input}"

    elif tool == "Summarizer":
        prompt = f"summarize this: {user_input}"

    elif tool == "FAQ Bot":
        prompt = f"faq: {user_input}"

    elif tool == "Transfusion Predictor":
        if uploaded_file and uploaded_file.name.endswith(".csv"):
            import pandas as pd
            df = pd.read_csv(uploaded_file)
            from tools.transfusion_predictor.predict import predict_from_csv
            result = predict_from_csv(df)
            st.success(f"Prediction: {result}")
            st.stop()
        else:
            st.warning("Please upload a valid CSV file.")
            st.stop()

    elif tool == "OCR Reader":
        if uploaded_file:
            from tools.ocr_reader.read import extract_text_from_image
            with open("temp_img.png", "wb") as f:
                f.write(uploaded_file.read())
            result = extract_text_from_image("temp_img.png")
            st.success("Extracted Text:")
            st.text(result)
            st.stop()
        else:
            st.warning("Please upload an image.")
            st.stop()

    elif tool == "Full Pipeline":
        if uploaded_file:
            from tools.ocr_reader.read import extract_text_from_image
            from tools.summarizer.summarize import generate_summary
            from tools.transfusion_predictor.predict import predict_from_summary

            with open("temp_img.png", "wb") as f:
                f.write(uploaded_file.read())

            ocr_text = extract_text_from_image("temp_img.png")
            st.info("✅ OCR Extracted Text:")
            st.text(ocr_text)

            summary = generate_summary(ocr_text)
            st.info("✅ Summarized Report:")
            st.text(summary)

            result = predict_from_summary(summary)
            st.success(f"🩸 Predicted Next Transfusion Date: {result}")
            st.stop()
        else:
            st.warning("Please upload an image.")
            st.stop()

    # Route user input to agent for other tools
    if prompt:
        response = controller.run(prompt)
        st.success(response)