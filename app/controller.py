# app/controller.py

import time
from app.memory import ChatMemory

class AgentController:
    def __init__(self, user_language='en'):
        self.memory = ChatMemory()
        self.user_language = user_language

    def run(self, user_input):
        """
        Main entry point from Streamlit UI
        """

        from app.router import route_to_tool

        # Save user input
        self.memory.add_message('user', user_input)

        # Route to appropriate tool
        tool_response = route_to_tool(user_input, self.memory, self.user_language)

        # Save tool response
        self.memory.add_message('agent', tool_response)

        return tool_response

    def reset_conversation(self):
        self.memory.reset()