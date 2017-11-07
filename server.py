#-*- encoding:utf-8 -*-
from flask import Flask, make_response, redirect
from flask_cors import CORS 
import json

app = Flask(__name__)
app.debug = True
CORS(app)

####
def response(data, status=200):
	resp = make_response(json.dumps(data), status)
	resp.mimetype = 'application/json'
	return resp
####

@app.route('/')
def index():
	data = {"hello":"hello world man"}
	return response(data, 200)

if __name__ == '__main__':
	app.run()