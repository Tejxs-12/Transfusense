import os
import sys

# Add app and tools directory to sys.path
sys.path.insert(0, os.path.abspath('./app'))
sys.path.insert(0, os.path.abspath('./tools/translator'))
sys.path.insert(0, os.path.abspath('./tools/intent_classifier'))
sys.path.insert(0, os.path.abspath('./tools/summarizer'))
sys.path.insert(0, os.path.abspath('./tools/transfusion_predictor'))
sys.path.insert(0, os.path.abspath('./tools/faq_bot'))
sys.path.insert(0, os.path.abspath('./tools/ocr_reader'))

# Import modules to test
from tools.translator.translator import translate_text
from tools.intent_classifier.classify import classify_intent
from tools.summarizer.summarize import summarize_text
from tools.transfusion_predictor.predict import predict_next_transfusion_date
from tools.faq_bot.faq_bot import get_faq_response
from tools.ocr_reader.read import extract_text_from_image


def test_translator():
    print("\n✅ Testing Translator")
    result = translate_text("Hello, how are you?", source_lang="en", target_lang="hi")
    print("Translated to Hindi:", result)


def test_classifier():
    print("\n✅ Testing Intent Classifier")
    result = classify_intent("When is my next transfusion?")
    print("Intent:", result)


def test_summarizer():
    print("\n✅ Testing Summarizer")
    sample_text = "Patient shows signs of anemia. Hemoglobin count is low. Recommend transfusion next week."
    summary = summarize_text(sample_text)
    print("Summary:", summary)


from tools.transfusion_predictor.predict import predict_from_csv

def test_transfusion_predictor():
    print("\n✅ Testing Transfusion Predictor")
    result = predict_from_csv("./data/transfusion_data.csv")
    print("Next predicted date:", result)


def test_faq_bot():
    print("\n✅ Testing FAQ Bot")
    result = get_faq_response("What is thalassemia?")
    print("FAQ Answer:", result)


# ✅ Testing OCR Reader
print("\n✅ Testing OCR Reader")
ocr_image_paths = [
    "assets/example_images/sample_report.png",
    "assets/example_images/sample_report.jpg"
]

ocr_tested = False
for path in ocr_image_paths:
    if os.path.exists(path):
        text = extract_text_from_image(path)
        print(f"OCR Extracted Text:\n{text}")
        ocr_tested = True
        break

if not ocr_tested:
    print("⚠️ OCR test skipped. Add sample_report.png or sample_report.jpg in assets/example_images/")