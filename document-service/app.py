from flask import Flask, request, jsonify
from PyPDF2 import PdfReader
from docx import Document
import os

app = Flask(__name__)

@app.route('/api/documents/upload', methods=['POST'])
def upload_document():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    # Save file to temp path
    file_path = f"/tmp/{file.filename}"
    file.save(file_path)

    # Handle PDF
    if file.filename.endswith('.pdf'):
        try:
            reader = PdfReader(file_path)
            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""
            return jsonify({"text": text})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    # Handle DOCX
    elif file.filename.endswith('.docx'):
        try:
            doc = Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])
            return jsonify({"text": text})

        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Unsupported file type"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
