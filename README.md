# 🎓 AI Multi-Agent QCM Generator (Windows Edition)

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/LLM-Groq-orange?logo=rocket&logoColor=white)](https://groq.com/)
[![Google Cloud](https://img.shields.io/badge/Google-Forms_API-4285F4?logo=google-cloud&logoColor=white)](https://console.cloud.google.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A powerful, automated system that leverages **Multi-Agent AI** to generate high-quality Multiple Choice Questions (QCM), validate them, and deploy them directly to Google Forms.

## ✨ Features

- 🧠 **Smart Generation**: Leverages the lightning-fast **Groq API** (Llama models) to generate pedagogically sound questions.
- ✅ **Automated Validation**: Dedicated validator agent ensures question integrity and strictly formats AI output using Regex.
- 📝 **Google Forms Integration**: Automatically creates and populates a Google Form with the generated questions using OAuth 2.0 User Credentials.
- 📄 **PDF Correction Sheets**: Generates a professional PDF correction file for offline review.
- 🎯 **Customizable Difficulty**: Supports `easy`, `medium`, and `hard` levels for any given topic.

## 🏗️ Architecture

The project follows a modular multi-agent and service-oriented architecture:

### 🤖 Agents
- **`QuestionGenerator`**: Interfaces with Groq to brainstorm and format questions based on the provided topic. Includes Regex parsing to handle conversational AI output gracefully.
- **`QuestionValidator`**: Performs structural and logical validation of the generated JSON data.

### 🛠️ Services
- **`GoogleFormsService`**: Handles OAuth 2.0 authentication (via browser pop-up) and interacts with the Google Forms API v1.
- **`PDFGenerator`**: Uses `ReportLab` to construct professional correction documents.
- **`Config`**: Centralized management of API keys, paths, and model parameters loaded seamlessly via `.env`.

## 🚀 Getting Started for Windows Users

### 1️⃣ Prerequisites
- Python **3.10** or higher installed on your Windows machine.
- A **Groq API Key** (get one at [console.groq.com](https://console.groq.com/)).
- A **Google Cloud Project** with the Forms API enabled.
- An **OAuth 2.0 Client ID** (Desktop App) downloaded as `client_secret.json`.

### 2️⃣ Installation
Open your Command Prompt (`cmd`) or PowerShell and run:
```cmd
:: Clone the repository
git clone <repository-url>
cd qcm-generator

:: Setup virtual environment
python -m venv venv
venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt
```

### 3️⃣ Configuration
Create a file named `.env` in the root folder of the project. Add the following lines to it:
```env
GROQ_API_KEY="your_groq_api_key_here"
GOOGLE_CREDENTIALS_PATH="credentials/client_secret.json"
```

> [!IMPORTANT]
> Ensure your downloaded Google OAuth file is placed in the `credentials/` folder and is named exactly `client_secret.json`.

## 🎮 Usage

Run the main script and follow the interactive prompts:
```cmd
python main.py
```

**Workflow:**
1. ⌨️ **Input Topic**: e.g., "Web Development"
2. 🎚️ **Select Difficulty**: `easy`, `medium`, or `hard`
3. 🔐 **Authentication**: On your first run, a web browser will open. Select your Google account and grant permission to manage Google Forms. This will create a `token.json` file for future use.
4. ⚙️ **Automatic Processing**: Generation -> Validation -> Form Creation -> PDF Generation
5. 🎉 **Output**: Get your Google Form URL and the PDF path!

## 📂 Project Structure

```text
qcm-generator/
├── agents/             # AI logic for generation and validation
├── services/           # External API integrations (Forms, PDF)
├── credentials/        # Storage for Google API JSON files and auth tokens
├── output/             # Generated JSON and PDF files
├── config.py           # Configuration manager
├── .env                # Environment variables (Create this file!)
└── main.py             # Application entry point
```

## 🛠️ Troubleshooting

- **Access Blocked (Google Verification)**: If you get a Google warning saying the app is blocked, go to your Google Cloud Console -> **OAuth consent screen** -> **Test users** and add your `@gmail.com` address. Then click "Advanced -> Go to QCM_generator (unsafe)" when logging in.
- **Quota Exceeded Error**: By using OAuth 2.0 (`client_secret.json`) instead of a Service Account, the script uses your personal 15GB Google Drive quota, fully resolving the infamous 0-byte Service Account creation limit.
- **Module Not Found**: Ensure you have activated your virtual environment using `venv\Scripts\activate` before running `python main.py`.

---
Built with ❤️ by Nour Omri & Halim Choukani.
