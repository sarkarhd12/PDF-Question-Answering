PDF Question-Answering Backend Service
Overview

This backend service enables users to upload PDF documents and ask questions based on the document's content. Utilizing natural language processing (NLP) with LangChain or LlamaIndex, it provides real-time responses to questions via WebSocket, supporting follow-up questions within the same context.
Tech Stack

    Backend Framework: FastAPI
    WebSocket Support: FastAPI's WebSocket integration
    NLP Processing: LangChain/LlamaIndex
    Database: SQLite (default) or PostgreSQL
    File Storage: Local filesystem or AWS S3 (optional)
    Testing: Pytest and Unittest

Features

    PDF Upload:
        Accepts PDF uploads via a REST API.
        Extracts and stores text for efficient querying.

    Real-Time Question Answering:
        Uses WebSocket to handle question-answering in real-time.
        Maintains session-based context for follow-up questions.

    Rate Limiting:
        Applies limits to the number of API requests and WebSocket messages per user.

    Data Management:
        Stores document metadata (filename, upload date).
        Extracts and stores PDF text content for NLP processing.

Installation and Setup

    Clone the Repository:

    bash

git clone https://github.com/sarkarhd12/PDF-Question-Answering
cd backend-service

Install Requirements:

bash

pip install -r requirements.txt

Environment Configuration: Create a .env file with your OpenAI API key and database URL:

DATABASE_URL=sqlite:///./pdf_data.db  # Or PostgreSQL URL

Database Setup:

bash

python setup_database.py

Start the Service:

bash

    uvicorn main:app --reload

API Endpoints
1. PDF Upload Endpoint

    Method: POST
    URL: /upload-pdf
    Description: Accepts a PDF file, extracts text, and saves the file and metadata.
    Response: Returns file ID and upload status.

2. WebSocket Question Answering

    URL: /ws/question
    Description: WebSocket for asking questions based on uploaded PDFs.
    Usage: Send file ID and question text via WebSocket for real-time responses.

WebSocket Session

    Connect to the WebSocket endpoint.
    Send Messages in JSON format:

    json

{
  "file_id": "file_id_here",
  "question": "Your question here"
}

Receive Responses with relevant answers and context support for follow-up questions.#   P D F - Q u e s t i o n - A n s w e r i n g 
 
 
