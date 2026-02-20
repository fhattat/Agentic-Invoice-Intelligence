import PIL.Image
from pypdf import PdfReader
import io

def load_document(file):
    """
    Yüklenen dosyayı (PDF veya Image) AI modelinin anlayacağı formata dönüştürür.
    """
    if file.type == "application/pdf":
        # PDF dosyasını metne çevir
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    else:
        # Görsel dosyası ise (JPG, PNG)
        image = PIL.Image.open(file)
        return image