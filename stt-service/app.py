import speech_recognition as sr
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/stt/transcribe', methods=['POST'])
def transcribe():
    file = request.files['file']  # Get the audio file from the request
    recognizer = sr.Recognizer()
    with sr.AudioFile(file) as source:
        audio = recognizer.record(source)  # Capture audio from the file

    try:
        text = recognizer.recognize_google(audio)  # Convert speech to text using Google Web Speech API
        return jsonify({"transcription": text})
    except sr.UnknownValueError:
        return jsonify({"error": "Could not understand the audio"}), 400
    except sr.RequestError:
        return jsonify({"error": "Request failed"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
