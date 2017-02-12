import requests
import json
from pprint import pprint
from google.cloud import translate

image_url = "http://i.imgur.com/B12UFBn.png"
headers = {"ocp-apim-subscription-key": "f560dba46ad945feaadeaab2846ea16c", "content-type": "application/json"}
payload = {"language": "unk", "orientation": "true"}
data = {"url": image_url}


r = requests.post("https://westus.api.cognitive.microsoft.com/vision/v1.0/ocr", params=payload, headers=headers, data=json.dumps(data))

result = r.json()
sentences = []
translated_sentences = []

for s in result["regions"][0]["lines"]:
    sentence = ""

    for word in s["words"]:
        sentence += word["text"]

    sentences.append(sentence)

pprint(sentences)

translate_client = translate.Client()
target = "en"

for s in sentences:
    sentence = translate_client.translate(s, target_language=target)["translatedText"]
    translated_sentences.append(sentence)

pprint(translated_sentences)
