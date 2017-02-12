import requests
import json
from pprint import pprint

MICROSOFT_API_KEY = "YOUR API KEY"
GOOGLE_API_KEY = "YOUR API KEY"

image_url = input("Enter an image URL to one of the pages in a manga chapter: ")
headers = {"ocp-apim-subscription-key": MICROSOFT_API_KEY, "content-type": "application/json"}
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

for s in sentences:
    data = {"target": "en", "key": GOOGLE_API_KEY, "q": s}
    r = requests.get("https://translation.googleapis.com/language/translate/v2", params=data)
    result = r.json()
    
    sentence = r.json()["data"]["translations"][0]["translatedText"]
    translated_sentences.append(sentence)

pprint(translated_sentences)
