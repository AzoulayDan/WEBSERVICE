DROP TABLE IF EXISTS Compte CASCADE;

CREATE TABLE Compte(
	id_compte		SERIAL PRIMARY KEY,
	login_compte		Varchar(25),
	password_compte		Varchar(25),
	role_compte		Varchar(25)
);

INSERT INTO Compte(login_compte, password_compte, role_compte) VALUES
	('toto','password','admin'),
	('babar', 'password2', 'team'),
	('elephant', 'password3', 'coucou');

