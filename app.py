from setup import loadNgram, loadAttachGram, predictDiscordMessage
from flask import Flask, jsonify, request
import requests
import os 
from dotenv import load_dotenv

app = Flask(__name__)


load_dotenv()
apiKey = os.getenv("API_KEY")

def thesaurus(word):
    url = (f'https://api.api-ninjas.com/v1/thesaurus?word={word}')
    res = requests.get(url, headers={'X-Api-Key': apiKey})
    if res.status_code == requests.codes.ok:
        return (res.json())
    else:
        return ("Error:", res.status_code, res.text)

def antonym(thes):
    # tweaking weather its a random antonym or something else
    return thes["antonyms"][0]
    # pass

@app.route("/", methods=["GET", "PAW"])
def defaultPredict():
    test = loadNgram("nGram.json")
    att = loadAttachGram("attachments.json")
    mes = predictDiscordMessage(test, att)
    return mes

@app.route("/evil", methods=["GET", "PAW"])
def evilPredict():
    test = loadNgram("nGram.json")
    att = loadAttachGram("attachments.json")
    mes = predictDiscordMessage(test, att)
    mes["evil_message"] = ""
    
    for x in mes["message"].split():
        th = thesaurus(x)
        if th["antonyms"]:
            e = antonym(th)
            mes["evil_message"] += e + " "
        else:
            mes["evil_message"] += x + " "
    mes["evil_message"] = mes["evil_message"][:-1]


    return mes

if __name__ == '__main__':
    app.run()