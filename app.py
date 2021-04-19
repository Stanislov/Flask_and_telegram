# coding: utf8


from flask import Flask, request
import requests


app = Flask(__name__)

def get_weather():
    params = {"access_key": "c5fe3e8f3ad6cd49b2690908ec593544", "query": "Moscow"}
    api_result = requests.get('http://api.weatherstack.com/current', params)
    api_response = api_result.json()
    
    print('\n', '--------------------------', '\n', api_response, '\n', '--------------------------', '\n')
    return f"Now in Moscow {api_response['current']['temperature']}'"

def send_message(chat_id, text):
    method = "sendMessage"
    token = "token" # add token
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["GET", "POST"])

def receive_update():
    if request.method == "POST":
        print(request.json)
        chat_id = request.json["message"]["chat"]["id"]
        weather = get_weather()
        send_message(chat_id, weather)
    return {"ok": True}
