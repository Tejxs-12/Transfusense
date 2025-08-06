# --- router.py content ---
import time
from app.router import route_to_tool
from app.memory import ChatMemory

class HealthAgentController:
    def __init__(self, user_language='en'):
        self.memory = ChatMemory()
        self.user_language = user_language

    def handle_user_input(self, user_input):
        # Save user message to memory
        self.memory.add_message('user', user_input)

        # Route to appropriate tool based on input
        tool_response = route_to_tool(user_input, self.memory, self.user_language)

        # Save tool response to memory
        self.memory.add_message('agent', tool_response)

        return tool_response

    def reset_conversation(self):
        self.memory.reset()


# --- memory.py content ---
class ChatMemory:
    def __init__(self):
        self.history = []

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return self.history

    def reset(self):
        self.history = []


# --- config.py content ---
class AgentConfig:
    DEFAULT_LANGUAGE = 'en'
    SUPPORTED_LANGUAGES = ['en', 'hi', 'es', 'fr', 'de']  # Extendable
    TOOL_NAMES = [
        'translator',
        'intent_classifier',
        'summarizer',
        'transfusion_predictor',
        'faq_bot',
        'ocr_reader'
    ]
    DEBUG_MODE = False