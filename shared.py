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

def is_valid_data(data):
	'''
	Cette fonction permet de vérifier si la donnée reçue
	peut être traité par le serveur.
	Valeur de retour:
		* False si la donnée ne peut pas être traitée
		* True si la donnée peut être traitée
	'''
	if (data == None):
		return False
	if not (isinstance(data, dict)):
		return False
	return True

########on verra plus tard si oui ou non on va lutiliser
def bad_request(key='error'):
	'''
	Cette fonction permet de retourner le message d'erreur
	'Bad request' avec un status code de 400.
	'''
	error = {key:'Error 400 : Bad request'}
	return response(error, 400)