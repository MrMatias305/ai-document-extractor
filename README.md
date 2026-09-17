# AI Document Extractor — V1

A beginner-friendly AI application that uses an LLM to analyze a text document and extract useful information from it.

This is **Version 1 (V1)** of the project, built as part of my hands-on learning journey into:

* Prompt Engineering
* LLM Integrations
* AI Automation
* AI-assisted Software Development
* AI Research & Experimentation

---

## 🎯 Project Goal

The goal of V1 is to understand the basic workflow of integrating an LLM into a Python application.

Instead of manually analyzing a document, the application:

1. Reads a text document.
2. Sends the document to an LLM through an API.
3. Provides instructions describing the task.
4. Receives the model's response.
5. Displays the AI-generated result.

### Basic Architecture

```text
Text Document
      │
      ▼
    Python
      │
      ▼
   LLM API
      │
      ▼
 AI-generated
    response
```

---

## 🛠️ Technologies

* **Python**
* **OpenAI API**
* **OpenAI Python SDK**
* **python-dotenv**
* **Git / GitHub**

---

## 📁 Project Structure

```text
ai-document-extractor/
│
├── .env
├── .gitignore
├── main.py
├── README.md
│
├── documents/
│   └── meeting.txt
│
└── output/
```

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone <repository-url>
cd ai-document-extractor
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install openai python-dotenv
```

### 4. Configure the API key

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

The API key should **never be committed to Git**.

Add `.env` to `.gitignore`:

```text
.env
.venv/
__pycache__/
```

---

## ▶️ Running the Application

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Then run:

```bash
python main.py
```

The application reads the selected document and sends its contents to the LLM for analysis.

---

## 🧠 Prompt Engineering

V1 uses a task-specific prompt to tell the model what information to extract.

The prompt provides:

* A role
* A clear objective
* Information to extract
* Constraints
* Instructions about missing information

Example structure:

```text
You are a document information extraction system.

Analyze the provided document and extract:

1. document type
2. date
3. people mentioned
4. action items
5. deadlines
6. a short summary

Rules:
- Do not invent information.
- If information is missing, return null.
- Preserve dates when explicitly provided.
- Separate each action item.
```

This demonstrates an important principle of prompt engineering:

> **The quality of an AI workflow depends heavily on how clearly the task and constraints are defined.**

---

## 🧪 Example Input

Example document:

```text
Project Alpha Meeting

The team met on September 15, 2026.

Sarah mentioned that the backend API should be completed
by September 20.

David will prepare the database schema by September 18.

The n
```

