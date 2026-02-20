import streamlit as st
from core.document_loader import load_document
from core.agent import InvoiceAgent
import PIL.Image
import pandas as pd # Veri işleme için eklendi

# Sayfa Konfigürasyonu
st.set_page_config(page_title="Agentic Invoice Intelligence", page_icon="📄", layout="wide")

st.title("📄 Agentic Invoice Intelligence")
st.markdown("Yapay Zeka Destekli Akıllı Fatura Analiz Sistemi")
st.divider()

# Yan Menü (Sidebar)
st.sidebar.header("Ayarlar")
uploaded_file = st.sidebar.file_uploader("Fatura Yükle (PDF veya Görsel)", type=["pdf", "jpg", "jpeg", "png"])

# Ana Ekran
if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Fatura Önizleme")
        if uploaded_file.type == "application/pdf":
            st.info("PDF dosyası yüklendi. İçerik analiz ediliyor...")
        else:
            image = PIL.Image.open(uploaded_file)
            st.image(image, caption="Yüklenen Fatura", use_column_width=True)

    with col2:
        st.subheader("Yapay Zeka Analizi")
        
        with st.spinner("Agent faturayı inceliyor ve verileri doğruluyor..."):
            try:
                # 1. Dokümanı yükle
                doc_content = load_document(uploaded_file)
                
                # 2. Agent'ı çalıştır
                agent = InvoiceAgent()
                result = agent.process_invoice(doc_content)
                
                # 3. Sonuçları Göster
                st.success("Analiz Tamamlandı!")
                
                # Özet Bilgiler
                st.write(f"**Gönderen Firma:** {result.sender_company}")
                st.write(f"**Fatura Tarihi:** {result.invoice_date}")
                st.write(f"**Toplam Tutar:** {result.total_amount} {result.currency}")
                
                # Hatalı olan st.table yerine güvenli pandas dataframe kullanımı
                with st.expander("Fatura Kalemlerini Gör", expanded=True):
                    if result.items:
                        # Pydantic modellerinden oluşan listeyi DataFrame'e çeviriyoruz
                        items_list = [item.dict() for item in result.items]
                        df = pd.DataFrame(items_list)
                        
                        # Sütun isimlerini daha şık hale getirelim (isteğe bağlı)
                        df.columns = ["Açıklama", "Miktar", "Birim Fiyat", "Toplam"]
                        
                        st.dataframe(df, use_container_width=True)
                    else:
                        st.warning("Fatura kalemi bulunamadı.")
                
                with st.expander("Ham JSON Çıktısı"):
                    st.json(result.dict())

            except Exception as e:
                # Hata detayını terminalden de görmek için:
                print(f"Hata Detayı: {e}")
                st.error(f"Bir hata oluştu: {e}")
else:
    st.info("Lütfen analiz etmek için sol menüden bir fatura dosyası yükleyin.")