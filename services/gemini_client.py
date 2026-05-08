from groq.api import Client

class GroqClient:
    def __init__(self, api_key):
        self.client = Client(api_key=api_key)

    def generate_questions(self, prompt):
        response = self.client.generate(prompt)
        return response

# Updated to use GROQ Free API instead of Gemini
