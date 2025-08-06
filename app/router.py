from shared.common import translate_text
from tools.intent_classifier.classify import classify_intent
from tools.summarizer.summarize import generate_summary
from tools.transfusion_predictor.predict import predict_from_csv
from tools.faq_bot.faq_bot import get_faq_response
from tools.ocr_reader.read import extract_text_from_image


def route_to_tool(user_input, memory=None, user_language='en'):
    """
    Routes the input to appropriate tool based on classified intent.
    """

    # Step 1: Translate to English for classification
    translated_input = (
        translate_text(user_input, source_lang=user_language, target_lang='en')
        if user_language != 'en'
        else user_input
    )

    # Step 2: Classify intent
    intent = classify_intent(translated_input)

    # Step 3: Handle routing
    if intent == 'translate':
        response = translate_text(user_input, source_lang=user_language, target_lang='en')

    elif intent == 'summarize':
        response = generate_summary(translated_input)

    elif intent == 'predict_transfusion':
        response = predict_from_csv(translated_input)  # ✅ Fixed line

    elif intent == 'faq':
        response = get_faq_response(translated_input)

    elif intent == 'ocr_read':
        # Expect image input from memory or predefined source
        if memory and memory.last_image_path:
            response = extract_text_from_image(memory.last_image_path)
        else:
            response = "Please upload an image before using the OCR tool."

    else:
        response = "I'm sorry, I couldn't understand your request. Could you please rephrase it?"

    # Step 4: Translate response back to user language
    if user_language != 'en':
        response = translate_text(response, source_lang='en', target_lang=user_language)

    return response