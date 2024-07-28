"""Final Project: Emotion Detector"""

import requests
import json

def emotion_detector(text_to_analyse):
    '''Analyses the emotion conveyed by the input text'''

    url = ('https://sn-watson-emotion.labs.skills.network/'
        'v1/watson.runtime.nlp.v1/NlpService/EmotionPredict')
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header, timeout=10)
    formatted_response = json.loads(response.text)

    # Extract emotions
    if response.status_code == 200:
        emotions = formatted_response['emotionPredictions'][0]['emotion']
        # Find the dominant emotion
        emotions['dominant_emotion'] = max(zip(emotions.values(), emotions.keys()))[1]
    else:
        emotions = None

    # Return the text attribute of the response
    return emotions
