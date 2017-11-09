#-*- encoding:utf-8 -*-
from db import Db 

def check_device_exist(device_identifier):
	'''
	Cette fonction permet de vérifier l'existence d'un appareil en base de données.
	Valeur de retour:
		* True si l'appareil existe.
		* False si l'appareil n'existe pas.
	'''
	db = Db()
	count = db.select("SELECT COUNT(*) FROM Compte WHERE (device_identifier_compte = %(identifier)s)", {
		"identifier":device_identifier
		})
	db.close()

	if (count[0]['count'] == 1):
		return True
	return False


#to test
def check_login_exist(login):
	'''
	Cette fonction permet de vérifier l'existence du nom d'une équipe par rapport au paramètre login.
	Valeur de retour:
		* True si le nom de l'équipe existe déjà.
		* False si le nom de l'équipe n'existe pas.
	'''
	db = Db()
	count = db.select("SELECT COUNT(*) FROM Compte WHERE (login_compte = %(name_team)s)", {
		"name_team":login
		})
	db.close()
	
	if (count[0]['count'] == 1):
		return True
	return False
	

#To test
def create_gamer_account(login, password, identifier):
	'''
	Cette fonction permet de créer un nouveau compte gamer.
	Valeur de retour:
		* True si le compte est créée.
	'''
	db.execute("INSERT INTO Compte(login_compte, password_compte, role_compte, points_compte, \
		device_identifier_compte) VALUES (%(login)s, %(password)s, %(role)s, %(points)s, \
		%(identifier_device)s)", {
		"login":login,
		"password":password,
		"role":"team",
		"points":0,
		"identifier_device":identifier
	})
	return True














#A voir si on utilise ce qui se trouve dessous.
def check_login_infos(login, password):
	'''
	Cette fonction permet de vérifier les informations de connexions.
	Valeur de retour:
		* -2 si il y a un probleme en base de données
		* -1 si le compte n'existe pas.
		* 0 si le compte est un compte administrateur
		* 1 si le compte est un compte gamer
	'''
	return_value = -2
	db = Db()
	count = db.select("SELECT COUNT(*) FROM Compte WHERE (login_compte = %(a_login)s AND password_compte = %(a_password)s)", {
		"a_login":login,
		"a_password":password
		})
	
	if (count[0]['count'] == 0):
		return_value = -1
	else:
		role_array = db.select("SELECT role_compte FROM Compte WHERE (login_compte = %(a_login)s AND password_compte = %(a_password)s)", {
			"a_login":login,
			"a_password":password
			})

		if (len(role_array) == 1):
			role = role_array[0]['role_compte']
			print(role)

			if (role == 'admin'):
				return_value = 0
			elif (role == 'team'):
				return_value = 1
	db.close()
	return return_value

