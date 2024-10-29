
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_question_ws():
    async with client.websocket_connect("/ws/question") as websocket:
        
        await websocket.send_json({
            "file_id": "test_file_id",
            "question": "What is the content of the PDF?"
        })
        response = await websocket.receive_text()
        assert "answer" in response.lower()  

@pytest.mark.asyncio
async def test_websocket_invalid_file_id():
    async with client.websocket_connect("/ws/question") as websocket:
        
        await websocket.send_json({
            "file_id": "invalid_id",
            "question": "What is the content of the PDF?"
        })
        response = await websocket.receive_text()
        assert response == "Invalid file_id or question." 
