# tools/ocr_reader/read.py

import pytesseract
from PIL import Image
import os

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str) -> str:
    """
    Extracts text from a lab report image using OCR.
    :param image_path: Path to the image file
    :return: Extracted text as a string
    """
    if not os.path.exists(image_path):
        return f"❌ Image file does not exist at: {image_path}"

    try:
        # Open and convert image to RGB (ensures compatibility)
        image = Image.open(image_path).convert("RGB")

        # Perform OCR
        extracted_text = pytesseract.image_to_string(image)

        if not extracted_text.strip():
            return "⚠️ No readable text found in the image."

        return extracted_text.strip()

    except Exception as e:
        return f"❌ Error processing image: {str(e)}"