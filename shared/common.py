from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

try:
    model_name = "Helsinki-NLP/opus-mt-en-hi"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    translation_pipeline = pipeline("translation_en_to_hi", model=model, tokenizer=tokenizer)
except Exception as e:
    print(f"Translation pipeline failed to load: {e}")
    translation_pipeline = None

def translate_text(text: str, source_lang=None, target_lang=None) -> str:
    if not translation_pipeline:
        return "Translation not available"
    try:
        result = translation_pipeline(text)
        return result[0]['translation_text']
    except Exception as e:
        return f"Error during translation: {e}"