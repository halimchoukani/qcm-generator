# main.py

from agents.generator import QuestionGenerator
from agents.validator import QuestionValidator
from services.google_forms import GoogleFormsService
from services.pdf_generator import PDFGenerator
from config import Config
import json

def main():
    # Load configuration
    config = Config()

    # Get user input
    topic = input("Enter the topic for the QCM: ")
    difficulty = input("Enter difficulty level (easy/medium/hard): ")

    # Generate questions
    generator = QuestionGenerator(config)
    questions = generator.generate(topic, difficulty)

    # Validate questions
    validator = QuestionValidator()
    validated_questions = validator.validate(questions)

    # Save validated questions to JSON
    with open(config.output_json_path, 'w') as f:
        json.dump(validated_questions, f, indent=4)

    # Create Google Form
    forms_service = GoogleFormsService(config)
    form_url = forms_service.create_form(validated_questions)

    # Generate PDF
    pdf_generator = PDFGenerator(config)
    pdf_generator.generate(validated_questions)

    print("QCM generation complete!")
    print(f"Google Form URL: {form_url}")
    print(f"PDF saved at: {config.output_pdf_path}")

if __name__ == "__main__":
    main()
