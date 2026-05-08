# generator.py

from google.genai import Client
import json

class QuestionGenerator:
    def __init__(self, config):
        self.client = Client(api_key=config.gemini_api_key)
        self.model = config.gemini_model
        self.temperature = config.temperature

    def generate(self, topic, difficulty):
        prompt = (
            f"Generate 10 multiple-choice questions on the topic '{topic}' with {difficulty} difficulty. "
            "Each question must have exactly 4 choices and 1 correct answer. Return ONLY valid JSON."
        )
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        try:
            return response['contents']
        except KeyError:
            raise ValueError("Invalid response format from Gemini API")
