#-*- encoding:utf-8 -*-
from db import Db 

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

