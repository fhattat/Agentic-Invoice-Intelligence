import os
import json
import google.generativeai as genai
from core.parser import InvoiceData

class InvoiceAgent:
    def __init__(self):
        # Retrieve the API key from Streamlit Secrets or Environment Variables
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found! Set it in Streamlit Cloud Secrets.")
        
        genai.configure(api_key=api_key)
        
        # Select the best available model
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        if 'models/gemini-1.5-flash' in available_models:
            model_name = 'models/gemini-1.5-flash'
        elif 'models/gemini-1.5-pro' in available_models:
            model_name = 'models/gemini-1.5-pro'
        else:
            model_name = available_models[0]
            
        print(f"Using Active Model: {model_name}")
        self.model = genai.GenerativeModel(model_name)

    def process_invoice(self, document_content):
        # Get the JSON schema from the Pydantic model
        schema = InvoiceData.model_json_schema()
        
        # English System Prompt for high accuracy
        prompt = f"""
        You are an expert invoice analysis assistant. 
        Extract information from the provided document content and return it ONLY in JSON format.
        Do not provide any conversational text or explanations outside of the JSON.
        
        Follow this JSON Schema strictly:
        {json.dumps(schema, indent=2)}
        
        Document Content:
        {document_content}
        """
        
        # Call the LLM
        response = self.model.generate_content(prompt)
        
        # Clean the response to ensure valid JSON
        raw_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(raw_text)
        
        # Validate and return as an InvoiceData object
        return InvoiceData(**data)
