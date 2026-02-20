import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
from core.parser import InvoiceData

load_dotenv()

class InvoiceAgent:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY bulunamadı!")
        
        genai.configure(api_key=api_key)
        
        # 404 hatasını aşmak için sistemdeki aktif modelleri sorgula ve en iyisini seç
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # Tercih sırasına göre model seçimi
        if 'models/gemini-1.5-flash' in available_models:
            model_name = 'models/gemini-1.5-flash'
        elif 'models/gemini-1.5-pro' in available_models:
            model_name = 'models/gemini-1.5-pro'
        else:
            model_name = available_models[0] # Hiçbiri yoksa ilk bulduğunu seç
            
        print(f"Aktif Model Kullanılıyor: {model_name}")
        self.model = genai.GenerativeModel(model_name)

    def process_invoice(self, document_content):
        schema = InvoiceData.model_json_schema()
        
        prompt = f"""
        Sen uzman bir fatura analiz asistanısın. 
        Aşağıdaki döküman içeriğinden bilgileri çıkar ve SADECE JSON formatında döndür.
        JSON formatı dışına çıkma, açıklama yapma.
        
        JSON Şeması:
        {json.dumps(schema, indent=2)}
        
        İçerik:
        {document_content}
        """
        
        # API çağrısı
        response = self.model.generate_content(prompt)
        
        # Yanıtın içindeki JSON kısmını temizleme
        raw_text = response.text.replace("```json", "").replace("```", "").strip()
        data = json.loads(raw_text)
        
        return InvoiceData(**data)