import os
import base64
from mistralai import Mistral
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
MISTRAL_API_KEY=os.getenv("MISTRAL_API_KEY")
def extract_text(file):
    file_name=file.name
    extension=os.path.splitext(file_name)[1].lower()

    if extension=='.txt':
        return file.read().decode("utf-8")
    
    elif extension=='.pdf':
        content=file.read()
        encoded_pdf=base64.b64encode(content).decode("utf-8")
        client=Mistral(api_key=MISTRAL_API_KEY)

        response=client.ocr.process(
            model="mistral-ocr-latest",
            document={
        "type": "document_url",
        "document_url": f"data:application/pdf;base64,{encoded_pdf}" 
    }
        )

        return "\n\n".join([page.markdown for page in response.pages])
    else:
        return "Unsupported file format"
    

