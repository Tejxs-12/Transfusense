# memory.py

class ChatMemory:
    def __init__(self):
        self.history = []
        self.last_image_path = None  # 👈 NEW: Store path to uploaded image if any

    def add_message(self, role, content):
        self.history.append({"role": role, "content": content})

    def get_history(self):
        return self.history

    def reset(self):
        self.history = []
        self.last_image_path = None  # 👈 Reset image path as well

    def set_image_path(self, path):
        self.last_image_path = path