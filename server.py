#-*- encoding:utf-8 -*-
from flask import Flask, redirect, request
from flask_cors import CORS
from shared import *
from database_request import *

app = Flask(__name__)
app.debug = True
CORS(app)

@app.route('/')
def index():
	'''
	Cette route correspond à la racine du site.
	'''
	return redirect('debug/db/reset')

@app.route('/debug/db/reset', methods=['GET'])
def init_db():
	'''
	Cette route est utilisée pour initialiser la base de données.
	'''
	db = Db()
	db.executeFile('database.sql')
	db.close()
	return 'Database OK'

@app.route('/game/connect', methods=['POST'])
def connect_player():
	'''
	Cette route est utilisée pour connecter un joueur.
	Si l'appareil du joueur existe, on le connecte.
	Si l'appareil du joueur n'existe pas en base, il doit s'inscrire.
	Valeur de retour:
		* Appareil existent: {'exist':1}
		* Appareil n'existent pas: {'exist':0}
		* Bad request : {'exist':400}
	'''
	data = request.get_json()
	if (is_valid_data(data) == True): #Forme donnée valide
		if ('identifier_device' in data): #Key donnée valide
			device_exist = check_device_exist(data['identifier_device']) #Appareil existe en base?
			if (device_exist == True): # Existe
				return response({'exist':1})
			return response({'exist':0}) #Existe pas
		return response({'exist':400})
	return response({'exist':400})

@app.route('/game/team/create_account', methods=['POST'])
def create_account():
	'''
	Cette route est utilisée pour créer un nouveau un compte
	à un nouveau joueur.
	Valeur de retour:
		* Compte déjà existent: {'creation_game_account':409}
		* Compte créé : {'creation_game_account':201}
		* Bad request : {'creation_game_account':400}
	'''
	datas = request.get_json()
	if (is_valid_data(datas) == True):
		if ('login' in datas and 'password' in datas and 'identifier' in datas):
			if (check_login_exist(datas['login']) == True or check_device_exist(datas['identifier'])==True):
				return response({'creation_game_account':409})
			account_created = create_gamer_account(datas['login'], datas['password'], datas['identifier'])
			if (account_created == True):
				return response({'creation_game_account':201})
		return response({'creation_game_account':400})
	return response({'creation_game_account':400})

####Route de test bordel de chiot de merde
@app.route('/test', methods=['GET'])
def test():
	login_infos = check_login_infos('toto', 'password') #0
	login_infos2 = check_login_infos('babar', 'password2') #1
	login_infos3 = check_login_infos('elephant', 'password3') #-2
	login_infos4 = check_login_infos('thor', 'pasxk') #-1
	return response({"compte1":login_infos, "compte2":login_infos2, "compte3":login_infos3, "compte4":login_infos4}, 200)

@app.route('/deleteCompte',methods=['GET'])
def delete_count():
	db = Db()
	db.execute("DELETE FROM Compte")
	db.close()
	return response({'essaie':''})

#Structure des routes du web service entier (sans prendre en compte le docker)
#Le docker va être ensuite un second web service ou un morceau de code qui va être lancé avec une route.
#Tout ce qui suit dessous est a implémenté
########################
# Methodes GET
########################
@app.route('/admin/teams', methods=['GET'])
def get_infos_teams():
	'''
	Cette route est appelée lorsque l'administrateur
	de la solution désire l'ensemble des informations
	concernant les différentes teams.
	'''
	return 'différentes teams'

@app.route('/admin/teams/<team>', methods=['GET'])
def get_infos_team(team):
	'''
	Cette route est appelée lorsque l'administrateur
	de la solution désire l'ensemble des informations
	concernant une team.
	'''
	return 'infos a propos de une seule team'

@app.route('/game/mission/<team>', methods=['GET'])
def get_mission(team):
	'''
	Cette route est appelée lorsque l'on envoie une
	au client une mission pour une équipe en
	particulier.
	'''
	return 'envoyer une mission à une équipe en particulier'


########################
# Methodes POST
########################

@app.route('/game/validate_photo/<team>', methods=['POST'])
def validate_picture(team):
	'''
	Cette route est appelée lorsque le client vérifie
	si la photo qu'il a pris a été correcte ou non.
	A mettre ici l'analyse d'image ou non (reste à voir)
	'''
	return 'valider une image ici'

@app.route('/admin/connect', methods=['POST'])
def connect_admin():
	'''
	Cette route est appelée lors de la connection de
	l'administrateur de la solution.
	'''
	return 'connexion de admin'

if __name__ == '__main__':
	app.run()