import requests
import json

def emotion_detector(text_to_analyze):
    if text_to_analyze is None or text_to_analyze.strip() == "":
        return {"error": "Invalid input", "status_code": 400}

    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(URL, json=input_json, headers=header)

    if response.status_code != 200:
        return {"error": "API request failed", "status_code": response.status_code}

    data = json.loads(response.text)
    emotions = data["emotionPredictions"][0]["emotion"]
    dominant = max(emotions, key=emotions.get)

    return {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant,
        "status_code": 200
    }
