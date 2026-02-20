import PIL.Image
import io

def load_document(uploaded_file):
    """
    Converts the uploaded file into a format compatible with the Google Gemini API.
    """
    if uploaded_file.type == "application/pdf":
        # For PDF files, we send the raw bytes with the correct MIME type
        return {
            "mime_type": "application/pdf",
            "data": uploaded_file.read()
        }
    else:
        # For images, we open the image and return the PIL object or bytes
        image = PIL.Image.open(uploaded_file)
        return image
