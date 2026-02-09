# 🛡️ LLM Security Helper

A Streamlit application that analyzes code and application specifications for security vulnerabilities, mapping findings to OWASP Top 10 for LLM Applications and MITRE ATLAS frameworks.

## What It Does

**Part 1: Code Security Analysis**  
Input vulnerable code snippets → Get identified vulnerabilities and secure code fixes

**Part 2: Specification Vulnerability Assessment**  
Input GenAI/Agentic app specs → Get vulnerability report mapped to OWASP LLM Top 10 and MITRE ATLAS

## Installation

### 1. Clone & Install

```bash
git clone (https://github.com/ahlahaider/LLM-security-helper.git)
cd <your-repo-directory>
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_google_gemini_api_key_here
```

Get your API key at [Google AI Studio](https://aistudio.google.com/app/apikey)

## Usage

```bash
streamlit run app.py
```

Open `http://localhost:8501` and select your analysis type:
- **Part 1:** Paste code → Get vulnerabilities + secure fixes
- **Part 2:** Paste app specs → Get OWASP + MITRE mappings + mitigations

## Requirements

- Python 3.8+
- streamlit
- google-generativeai
- python-dotenv
- requests
