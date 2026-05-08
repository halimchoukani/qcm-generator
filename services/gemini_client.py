from google.genai.configuration import configure
from google.genai.model import Model

class GeminiClient:
    def __init__(self, api_key, model, temperature):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        configure(api_key=self.api_key)

    def generate_questions(self, prompt):
        response = Model(self.model).generate_content(prompt)
        return response
