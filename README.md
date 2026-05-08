# AI Multi-Agent QCM Generator

## Overview
This project generates a QCM (Questionnaire à Choix Multiples) based on a given topic, validates the questions, creates a Google Form, and generates a correction PDF.

## Features
- Generate 10 pedagogically relevant questions using Google Gemini API
- Validate questions for correctness and clarity
- Automatically create a Google Form with the questions
- Generate a PDF correction file

## Architecture
- **Agents**:
  - `generator.py`: Generates questions
  - `validator.py`: Validates questions
- **Services**:
  - `gemini_client.py`: Interacts with Google Gemini API
  - `google_forms.py`: Manages Google Forms
  - `pdf_generator.py`: Creates correction PDFs
- **Output**:
  - `qcm.json`: JSON file with validated questions
  - `correction.pdf`: PDF with questions and answers

## Prerequisites
1. Python 3.10 or higher
2. Install `pip` and `venv` if not already installed
3. Google API credentials JSON file

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd qcm-generator
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Set the following environment variables:
- `GEMINI_API_KEY`: Your Gemini API key
- `GOOGLE_CREDENTIALS_PATH`: Path to your Google credentials JSON file

Example:
```bash
export GEMINI_API_KEY="your-gemini-api-key"
export GOOGLE_CREDENTIALS_PATH="credentials/credentials.json"
```

### 5. Place Google Credentials
Ensure your Google credentials JSON file is located at `credentials/credentials.json`.

## Running the Application
```bash
python main.py
```

### Example Workflow
1. Enter the topic for the QCM (e.g., "Artificial Intelligence").
2. Enter the difficulty level (easy/medium/hard).
3. The application will:
   - Generate questions
   - Validate questions
   - Save validated questions to `output/qcm.json`
   - Create a Google Form and display the URL
   - Generate a correction PDF at `output/correction.pdf`

## Troubleshooting
- **Missing Dependencies**: Ensure `pip install -r requirements.txt` completes successfully.
- **Google API Errors**: Verify your credentials file and environment variable.
- **Gemini API Errors**: Ensure your API key is valid and has sufficient quota.

## Example Output
- **Google Form URL**: A link to the generated form
- **PDF Path**: `output/correction.pdf`

## License
This project is licensed under the MIT License.
