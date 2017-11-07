#-*- encoding:utf-8 -*-
from flask import Flask, redirect
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


@app.route('/test', methods=['GET'])
def test():
	login_infos = check_login_infos('toto', 'password') #0
	login_infos2 = check_login_infos('babar', 'password2') #1
	login_infos3 = check_login_infos('elephant', 'password3') #-2
	login_infos4 = check_login_infos('thor', 'pasxk') #-1
	return response({"compte1":login_infos, "compte2":login_infos2, "compte3":login_infos3, "compte4":login_infos4}, 200)

if __name__ == '__main__':
	app.run()