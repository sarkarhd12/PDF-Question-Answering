
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_upload_pdf():
   
    with open("sample.pdf", "rb") as pdf_file:
        response = client.post("/upload-pdf", files={"file": ("sample.pdf", pdf_file)})
    assert response.status_code == 200
    assert "file_id" in response.json()
    assert "metadata" in response.json()

def test_upload_non_pdf():

    with open("sample.txt", "rb") as text_file:
        response = client.post("/upload-pdf", files={"file": ("sample.txt", text_file)})
    assert response.status_code == 400
    assert response.json()["detail"] == "Invalid file type."

def test_rate_limit():
   
    for _ in range(10):  
        with open("sample.pdf", "rb") as pdf_file:
            response = client.post("/upload-pdf", files={"file": ("sample.pdf", pdf_file)})
    assert response.status_code == 429  
