# 📄 Agentic Invoice Intelligence

An AI-powered intelligent invoice analysis system focused on high accuracy and **Structured Data Extraction**. This project leverages multimodal Large Language Models (LLM) to transform unstructured data from PDF and image formats into validated, meaningful JSON structures.

## 🚀 Key Features

* **Multimodal Analysis:** Seamlessly processes invoices in both PDF and image (JPG, PNG) formats.
* **Structured Output:** Enforces LLM outputs using **Pydantic** schemas to ensure 100% data integrity and consistency.
* **AI Agent Workflow:** Extracts data with an expert perspective, accurately identifying complex line items, taxes (VAT, SCT), and tabular structures.
* **Dynamic Model Management:** Features a robust backend that queries active Google Gemini endpoints to automatically select the most stable model (Gemini 1.5 Pro/Flash).
* **Interactive Dashboard:** A user-friendly interface built with **Streamlit**, featuring interactive data tables powered by **Pandas**.

## 🛠️ Tech Stack

* **Language:** Python
* **AI Framework:** LangChain / Google Generative AI SDK
* **LLM Engine:** Google Gemini 1.5 Pro & Flash
* **Data Validation:** Pydantic
* **Frontend:** Streamlit
* **Data Handling:** Pandas

## 📦 Installation & Usage

1. **Clone the Repository:**
```bash
git clone https://github.com/doganhattatoglu/Agentic-Invoice-Intelligence.git
cd Agentic-Invoice-Intelligence

```


2. **Set Up Virtual Environment:**
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate

```


3. **Install Dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure API Key:**
Create a `.env` file in the root directory and add your Google AI Studio API key:
```text
GOOGLE_API_KEY=your_api_key_here

```


5. **Run the Application:**
```bash
streamlit run app.py

```



## 📂 Project Structure

```text
├── core/
│   ├── agent.py            # AI Agent logic & LLM configuration
│   ├── parser.py           # Pydantic data schemas
│   └── document_loader.py  # PDF/Image processing module
├── app.py                  # Streamlit frontend application
├── requirements.txt        # Project dependencies
└── .env                    # Environment variables (Sensitive Data)

```

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the `issues` page or submit a `pull request`.

---

Developed by **Fatih Hattatoglu** as part of an Advanced AI Engineering Portfolio.

