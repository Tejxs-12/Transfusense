# summarize.py
import pytesseract
from PIL import Image
from transformers import pipeline
import os

# Initialize summarizer pipeline with pretrained model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def extract_text_from_image(image_path):
    """Extract text using pytesseract from an image file."""
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"[OCR Error] {str(e)}"

def generate_summary(text_or_image_path):
    """Handle both raw text and image input, extract and summarize."""
    if os.path.isfile(text_or_image_path):
        extracted_text = extract_text_from_image(text_or_image_path)
    else:
        extracted_text = text_or_image_path

    if not extracted_text or len(extracted_text) < 20:
        return "Not enough content to summarize."

    try:
        summary = summarizer(extracted_text, max_length=300, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"[Summarization Error] {str(e)}"