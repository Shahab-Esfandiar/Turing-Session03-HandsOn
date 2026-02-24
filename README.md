# 📧 Automated AI Email Router
This project is an educational and high-performance AI engineering tool designed to demonstrate how Large Language Models (LLMs) can transform unstructured communications into structured, actionable data. It acts as an automated "Digital Receptionist," analyzing incoming organizational emails, extracting critical metadata, and dynamically routing them to the correct departmental endpoints.

## ✨ Key Features

**🧠 AI-Powered Analysis:** Uses advanced prompt engineering (Few-Shot & JSON-mode) to extract precise metadata including Category, Priority, a concise Summary, and Key Entities. 

**🌍 Bilingual Support:** Seamlessly processes both **English** and **Persian (Farsi)** emails. 

**🎨 Dynamic HTML Formatting:** Automatically detects text direction (RTL/LTR) based on the email content and generates a beautiful, responsive HTML report with a metadata table. 

**⚙️ Batch Processing & Mocking:** Includes a robust batch processing engine with many diverse mock scenarios (ranging from very short inquiries to long, complex complaints) to test the system without needing live email credentials. 

**🛡️ Robust Error Handling:** Features a custom exception management system (`LLMAnalysisError`, `MissingConfigurationError`) that isolates failures at the email level, allowing batch processes to continue uninterrupted even if individual API calls timeout.

**🧩 Modular Architecture:** Clean, object-oriented code separated into distinct modules (`analyzer`, `router`, `config`, `exceptions`) following software engineering best practices.



## 🏢 Organizational Departments (Routing Logic)

The AI categorizes and routes emails into one of the following internal addresses: 

1. `support@novinpardaz.com` -> **Technical Support** (Errors, server crashes, bugs) 
2. `sales@novinpardaz.com` -> **Sales & Billing** (Invoices, payments, quotes) 
3. `hr@novinpardaz.com` -> **HR** (Resumes, job applications, internships) 
4. `management@novinpardaz.com` -> **General** (Partnerships, complaints, unknown intents)



---

## 🛠️ Main  Services

* **Contextual Summarization:** Analyzes lengthy, complex emails and synthesizes the core user intent into a single-sentence `Summary` field.
* **Entity Extraction:** Automatically identifies and extracts crucial business parameters (e.g., error codes, invoice numbers, phone numbers) into a `Key_Entities` field for rapid human review.

### 🌐 Bilingual Data Processing
* **Native Multilingual Processing:** Effortlessly processes both English and Persian (Farsi) inquiries without requiring explicit translation pipelines, leveraging the inherent multilingual capabilities of GPT-4 class models.
* **Smart Categorization & Priority:** Evaluates the tone and keywords of the text to assign an operational `Category` (e.g., Technical Support, Sales, HR) and a `Priority` level (Low, Medium, High).

### 📥 Batch Testing & Mocking
* **Offline Mock Engine:** Includes a dedicated `mock_data` module featuring 20 diverse, real-world scenarios (ranging from brief 2-line inquiries to extensive 10-line technical complaints) to simulate high-volume inbox environments.
* **Automated Report Generation:** Bypasses live SMTP sending during testing to safely generate and save beautifully formatted, isolated `.html` files for every processed email into an `outputs/` directory.

### 🔒 Security & Standards
* **Environment Management:** Uses `python-dotenv` to keep API keys and server credentials completely secure and out of the version control system.
* **Type Hinting:** Fully annotated with Python typing (`Dict`, `Any`, `str`) for enterprise-grade readability, developer experience, and maintainability.

---

## 🚀 How to Run

1. **Clone the Repo**
2.  **Setup Virtual Environment & Install Requirements:**
    ```bash
    python -m venv venv
    # Windows: .\venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Setup Environment:**
    Create a `.env` file in the root directory and add your credentials:
    
    ```env
    AVALAI_API_KEY=your_api_key
    SYSTEM_EMAIL=dummy@test.com
    SYSTEM_PASSWORD=fake_password
    ```
4.  **Launch Batch Processor:**
    ```bash
    python main.py
    ```

---

## 🛠️ Tech Stack
* **Language:** Python 3.12+
* **AI Providers:** OpenAI API Interface (`gpt-4o`  via Avalai)
* **Core Libraries:** `json`, `re`, `os`, `typing`
* **Environment & Security:** `python-dotenv`
* **Architecture Style:** Object-Oriented Programming (OOP), Batch Processing Pipeline
