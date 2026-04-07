from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    text = request.json.get("text", "")
    result = emotion_detector(text)
    return jsonify(result)

if __name__ == "__main__":
    app.run()
