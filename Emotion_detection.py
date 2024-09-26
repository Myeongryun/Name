import requests

def predict_emotion(text):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    payload = {
        "emotion_detector": {
            "text": text
        }
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Error in calling Watson NLP service"}

if __name__ == "__main__":
    text_to_analyse = "I am so happy today!"
    result = predict_emotion(text_to_analyse)
    print(result)
