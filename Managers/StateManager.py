import json

class StateManager:
    def __init__(self, filename="bindings.json"):
        self.filename = filename

    def load_state(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_state(self, state):
        with open(self.filename, "w") as file:
            json.dump(state, file)