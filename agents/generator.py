# generator.py

import json
from groq import Groq


class QuestionGenerator:
    def __init__(self, config):
        self.config = config
        self.client = Groq(api_key=config.groq_api_key)

    def generate(self, topic, difficulty):
        prompt = f"""
Generate 10 multiple-choice questions about "{topic}" with "{difficulty}" difficulty.

Rules:
- Each question must contain:
  - question
  - 4 choices
  - correct
- The "correct" value MUST be the exact matching string from the "choices" array, NOT a letter (like A, B, C, D).
- Return ONLY valid JSON.
- Do not add explanations or markdown.

Expected JSON format:
[
  {{
    "question": "What is 2 + 2?",
    "choices": ["3", "4", "5", "6"],
    "correct": "4"
  }}
]
"""

        response = self.client.chat.completions.create(
            model=self.config.groq_model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=self.config.temperature,
        )

        import re
        content = response.choices[0].message.content

        # Extract the JSON array from the response, ignoring markdown or conversational text
        match = re.search(r'\[\s*\{.*\}\s*\]', content, re.DOTALL)
        if match:
            content = match.group(0)

        try:
            return json.loads(content)
        except json.JSONDecodeError:
            raise ValueError(
                f"Invalid JSON response from GROQ API:\n{content}"
            )