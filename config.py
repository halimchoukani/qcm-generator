import os

class Config:
    def __init__(self):
        self.groq_api_key = os.getenv(
            "GROQ_API_KEY",
            "your-groq-api-key"
        )
        # Updated to use GROQ Free API instead of Gemini

        self.google_credentials_path = os.getenv(
            "GOOGLE_CREDENTIALS_PATH",
            "credentials/credentials.json"
        )

        self.output_json_path = "output/qcm.json"
        self.output_pdf_path = "output/correction.pdf"

        self.default_difficulty = "medium"

        # Gemini model
        self.gemini_model = "gemini-2.5-flash"

        # Generation settings
        self.temperature = 0.7