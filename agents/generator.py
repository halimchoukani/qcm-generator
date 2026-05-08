# generator.py

import json
from groq import Groq


class QuestionGenerator:
    def __init__(self, config):
        # GROQ_API_KEY must be set in environment variables
        self.client = Groq(api_key=config.groq_api_key)

    def generate(self, topic, difficulty):
        prompt = f"""
Generate 10 multiple-choice questions about "{topic}" with "{difficulty}" difficulty.

Rules:
- Each question must contain:
  - question
  - 4 choices
  - correct_answer
- Return ONLY valid JSON.
- Do not add explanations or markdown.

Expected JSON format:
[
  {{
    "question": "Question text",
    "choices": ["A", "B", "C", "D"],
    "correct_answer": "A"
  }}
]
"""

        response = self.client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            raise ValueError(
                f"Invalid JSON response from GROQ API:\n{content}"
            )