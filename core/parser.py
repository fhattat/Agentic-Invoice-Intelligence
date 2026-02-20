from pydantic import BaseModel, Field
from typing import List, Optional

class InvoiceItem(BaseModel):
    description: str = Field(description="Description of the product or service")
    quantity: float = Field(description="Quantity of the item")
    unit_price: float = Field(description="Price per unit")
    total_price: float = Field(description="Total price for this line item")

class InvoiceData(BaseModel):
    sender_company: str = Field(description="The name of the company that issued the invoice")
    invoice_date: str = Field(description="Date of the invoice")
    total_amount: float = Field(description="The final total amount of the invoice")
    currency: str = Field(description="Currency used in the invoice (e.g., USD, TRY, EUR)")
    items: List[InvoiceItem] = Field(description="List of all products or services listed in the invoice")
