#-*- encoding:utf-8 -*-
from flask import Flask, make_response, redirect
from flask_cors import CORS 
import json
from db import Db

app = Flask(__name__)
app.debug = True
CORS(app)

####
def response(data, status=200):
	resp = make_response(json.dumps(data), status)
	resp.mimetype = 'application/json'
	return resp

def test():
	db = Db()
	count = db.select("SELECT COUNT(*) FROM Compte")
	print(count)
	db.close()
	return count
####

@app.route('/debug/db/reset', methods=['GET'])
def init_db():
	db = Db()
	db.executeFile('database.sql')
	db.close()
	return 'Database OK'

@app.route('/')
def index():
	essaie = test()
	data = {"hello":"hello world man", "test":essaie}
	return response(data, 200)

if __name__ == '__main__':
	app.run()