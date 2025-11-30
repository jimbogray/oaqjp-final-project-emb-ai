import requests
import json

WATSON_URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
WATSON_HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze):
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(WATSON_URL, headers=WATSON_HEADERS, json=data)
    response = json.loads(response.text)

    return response['emotionPredictions'][0]['emotionMentions'][0]['span']['text']

def main():
    print( emotion_detector("i love cheese and bread, my son") )

if __name__=="__main__":
    main()