from gtts import gTTS
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/tts/synthesize', methods=['POST'])
def synthesize():
    text = request.json.get('text', '')
    if not text:
        return jsonify({"error": "No text provided"}), 400
    tts = gTTS(text)
    tts.save('output.mp3')
    return jsonify({"message": "Audio generated successfully", "audio_file": "output.mp3"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
