from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

# Hardcoded lang_code_to_id values (needed because tokenizer doesn't support it)
LANG_CODE_TO_ID = {
    "afr_Latn": 0, "eng_Latn": 128112, "hin_Deva": 126052, "mar_Deva": 126275,
    "ben_Beng": 125994, "tam_Taml": 126308, "tel_Telu": 126326,
    "guj_Gujr": 126111, "kan_Knda": 126179, "mal_Mlym": 126253,
    # Add more as needed based on tokenizer.lang_code_to_id values
}

LANG_CODE = {
    "en": "eng_Latn",
    "hi": "hin_Deva",
    "mr": "mar_Deva",
    "bn": "ben_Beng",
    "ta": "tam_Taml",
    "te": "tel_Telu",
    "gu": "guj_Gujr",
    "kn": "kan_Knda",
    "ml": "mal_Mlym",
    # Extend as needed
}

# Load model and tokenizer
try:
    tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M", use_fast=False)
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    print("Device set to use", device)
except Exception as e:
    print("Translation pipeline failed to load:", e)
    tokenizer = None
    model = None

def translate_text(text: str, source_lang="en", target_lang="hi") -> str:
    if not tokenizer or not model:
        return "Translation not available"

    try:
        src_code = LANG_CODE.get(source_lang, "eng_Latn")
        tgt_code = LANG_CODE.get(target_lang, "hin_Deva")

        tokenizer.src_lang = src_code
        encoded = tokenizer(text, return_tensors="pt").to(device)
        forced_bos_token_id = LANG_CODE_TO_ID[tgt_code]

        generated_tokens = model.generate(
            **encoded,
            forced_bos_token_id=forced_bos_token_id
        )

        translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
        return translated_text
    except Exception as e:
        return f"Error during translation: {e}"

def detect_language_code(text: str) -> str:
    return "en"  # Stub (you can improve with langdetect)