#-*- encoding:utf-8 -*-
from flask import make_response
import json

def response(data, status=200):
	'''
	Cette fonction met en forme la donnée au format json
	'''
	resp = make_response(json.dumps(data), status)
	resp.mimetype = 'application/json'
	return resp

