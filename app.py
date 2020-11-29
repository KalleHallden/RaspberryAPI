from flask import Flask, request
import requests
import json
from tokens import get_tokens

tokens = get_tokens()

bridge_ip = tokens['BRIDGE_IP']
api_key = tokens['API_KEY']

url = 'http://' + bridge_ip + '/api/' + api_key + '/'
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello kalle'
@app.route('/lights', methods=['GET'])
def get_lights():
    r = request
    if r.method == 'GET':
        return request.get(url + 'lights').json()
@app.route('/lightsoff', methods=['GET'])
def lights_off():
    r = request
    if r.method == 'GET':
        return requests.put(url + 'lights/1/state', data = json.dumps({'on':False}))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
