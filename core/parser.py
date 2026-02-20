from pydantic import BaseModel, Field
from typing import List, Optional

class InvoiceItem(BaseModel):
    """Fatura içindeki her bir ürün veya hizmet kalemi"""
    description: str = Field(description="Ürün veya hizmetin açıklaması")
    quantity: float = Field(description="Miktar")
    unit_price: float = Field(description="Birim fiyat")
    total_price: float = Field(description="Kalemin toplam tutarı")

class InvoiceData(BaseModel):
    """Faturadan çekilecek ana veri yapısı"""
    sender_company: str = Field(description="Faturayı gönderen şirketin adı")
    recipient_company: str = Field(description="Faturanın kesildiği (alıcı) şirketin adı")
    invoice_date: str = Field(description="Fatura tarihi (GG/AA/YYYY formatında)")
    invoice_number: str = Field(description="Fatura numarası")
    items: List[InvoiceItem] = Field(description="Faturadaki ürünlerin listesi")
    tax_amount: float = Field(description="Toplam KDV tutarı")
    total_amount: float = Field(description="Her şey dahil genel toplam tutar")
    currency: str = Field(description="Para birimi (TRY, USD, EUR vb.)")