# google_forms.py

from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
import os

class GoogleFormsService:
    def __init__(self, config):
        self.credentials_path = config.google_credentials_path
        self.token_path = "credentials/token.json"
        self.scopes = ["https://www.googleapis.com/auth/forms.body"]
        self.credentials = self.authenticate()
        self.forms_service = build("forms", "v1", credentials=self.credentials, cache_discovery=False)

    def authenticate(self):
        creds = None
        # The file token.json stores the user's access and refresh tokens
        if os.path.exists(self.token_path):
            creds = Credentials.from_authorized_user_file(self.token_path, self.scopes)
        
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    self.credentials_path, self.scopes)
                creds = flow.run_local_server(port=0)
            
            # Save the credentials for the next run
            with open(self.token_path, 'w') as token:
                token.write(creds.to_json())
        return creds

    def create_form(self, questions):
        try:
            # 1. Create an empty form (Only title is allowed here)
            form_metadata = {
                "info": {"title": "Generated QCM"}
            }
            form = self.forms_service.forms().create(body=form_metadata).execute()
            form_id = form.get("formId")
            print(f"Created empty form with ID: {form_id}")

            # 2. Add questions using batchUpdate
            requests = {
                "requests": [
                    {
                        "createItem": {
                            "item": {
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
                            },
                            "location": {"index": i}
                        }
                    } for i, q in enumerate(questions)
                ]
            }

            self.forms_service.forms().batchUpdate(formId=form_id, body=requests).execute()
            
            # Retrieve the final form for the URL
            updated_form = self.forms_service.forms().get(formId=form_id).execute()
            return updated_form.get("responderUri")

        except HttpError as e:
            print("Google Forms API Error:")
            print(e)
            return None

