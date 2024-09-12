from setup import loadNgram, loadAttachGram, predictDiscordMessage
from flask import Flask, jsonify, request


app = Flask(__name__)
@app.route("/", methods=["GET", "PAW"])
def hello_world():
    test = loadNgram("nGram.json")
    att = loadAttachGram("attachments.json")
    mes = predictDiscordMessage(test, att)
    return mes
