import streamlit as st
from core.document_loader import load_document
from core.agent import InvoiceAgent
import PIL.Image
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Agentic Invoice Intelligence", page_icon="📄", layout="wide")

st.title("📄 Agentic Invoice Intelligence")
st.markdown("AI-Powered Smart Invoice Analysis System")
st.divider()

# Sidebar Configuration
st.sidebar.header("Settings")
uploaded_file = st.sidebar.file_uploader("Upload Invoice (PDF or Image)", type=["pdf", "jpg", "jpeg", "png"])

# Main Application Logic
if uploaded_file is not None:
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Invoice Preview")
        if uploaded_file.type == "application/pdf":
            st.info("PDF file uploaded. Analyzing content...")
        else:
            image = PIL.Image.open(uploaded_file)
            st.image(image, caption="Uploaded Invoice", use_column_width=True)

    with col2:
        st.subheader("AI Analysis Results")
        
        with st.spinner("Agent is analyzing the invoice and validating data..."):
            try:
                # 1. Load document content
                doc_content = load_document(uploaded_file)
                
                # 2. Initialize Agent and process the invoice
                agent = InvoiceAgent()
                result = agent.process_invoice(doc_content)
                
                # 3. Display Results
                st.success("Analysis Completed Successfully!")
                
                # Summary Information
                st.write(f"**Sender Company:** {result.sender_company}")
                st.write(f"**Invoice Date:** {result.invoice_date}")
                st.write(f"**Total Amount:** {result.total_amount} {result.currency}")
                
                # Line Items Table
                with st.expander("View Invoice Line Items", expanded=True):
                    if result.items:
                        # Convert Pydantic models to a clean DataFrame
                        items_list = [item.dict() for item in result.items]
                        df = pd.DataFrame(items_list)
                        
                        # Set professional English column names
                        df.columns = ["Description", "Quantity", "Unit Price", "Total"]
                        
                        st.dataframe(df, use_container_width=True)
                    else:
                        st.warning("No line items found in this document.")
                
                # Raw JSON Output for developer debugging
                with st.expander("Raw JSON Output"):
                    st.json(result.dict())

            except Exception as e:
                # Log detailed error to console and show user-friendly message
                print(f"Error Details: {e}")
                st.error(f"An error occurred during processing: {e}")
else:
    st.info("Please upload an invoice file from the sidebar to begin analysis.")
