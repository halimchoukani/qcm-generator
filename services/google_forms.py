# google_forms.py

from googleapiclient.discovery import build
from google.oauth2 import service_account

class GoogleFormsService:
    def __init__(self, config):
        self.credentials_path = config.google_credentials_path
        self.service = self.authenticate()

    def authenticate(self):
        credentials = service_account.Credentials.from_service_account_file(
            self.credentials_path,
            scopes=["https://www.googleapis.com/auth/forms"]
        )
        return build("forms", "v1", credentials=credentials)

    def create_form(self, questions):
        form = {
            "info": {"title": "Generated QCM"},
            "items": [
                {
                    "title": q["question"],
                    "questionItem": {
                        "question": {
                            "required": True,
                            "choiceQuestion": {
                                "type": "RADIO",
                                "options": [{"value": c} for c in q["choices"]],
                                "shuffle": False
                            }
                        }
                    }
                } for q in questions
            ]
        }
        result = self.service.forms().create(body=form).execute()
        return result.get("responderUri")
