DROP TABLE IF EXISTS Compte CASCADE;
DROP TABLE IF EXISTS Mission CASCADE;
DROP TABLE IF EXISTS Photo CASCADE;

-- Table: Compte
CREATE TABLE Compte(
        id_compte       int NOT NULL ,
        login_compte    Varchar (35) ,
        password_compte Varchar (35) ,
        role_compte     Varchar (25) ,
        points_compte   Int ,
        PRIMARY KEY (id_compte ) ,
        UNIQUE (login_compte )
);

-- Table: Mission
CREATE TABLE Mission(
        id_mission   int NOT NULL ,
        name_mission Varchar (35) ,
        PRIMARY KEY (id_mission )
);

-- Table: Photo
CREATE TABLE Photo(
        id_photo   int NOT NULL ,
        name_photo Varchar (35) ,
        lieu_photo Varchar (60) ,
        PRIMARY KEY (id_photo ) ,
        UNIQUE (name_photo )
);

-- Table: participer
CREATE TABLE participer(
        id_compte  Int NOT NULL ,
        id_mission Int NOT NULL ,
        PRIMARY KEY (id_compte ,id_mission )
);


-- Table: avoir
CREATE TABLE avoir(
        id_photo   Int NOT NULL ,
        id_mission Int NOT NULL ,
        PRIMARY KEY (id_photo ,id_mission )
);


-- Table: trouver
CREATE TABLE trouver(
        id_compte Int NOT NULL ,
        id_photo  Int NOT NULL ,
        PRIMARY KEY (id_compte ,id_photo )
);

-- Alter table
ALTER TABLE participer ADD CONSTRAINT FK_participer_id_compte FOREIGN KEY (id_compte) REFERENCES Compte(id_compte);
ALTER TABLE participer ADD CONSTRAINT FK_participer_id_mission FOREIGN KEY (id_mission) REFERENCES Mission(id_mission);
ALTER TABLE avoir ADD CONSTRAINT FK_avoir_id_photo FOREIGN KEY (id_photo) REFERENCES Photo(id_photo);
ALTER TABLE avoir ADD CONSTRAINT FK_avoir_id_mission FOREIGN KEY (id_mission) REFERENCES Mission(id_mission);
ALTER TABLE trouver ADD CONSTRAINT FK_trouver_id_compte FOREIGN KEY (id_compte) REFERENCES Compte(id_compte);
ALTER TABLE trouver ADD CONSTRAINT FK_trouver_id_photo FOREIGN KEY (id_photo) REFERENCES Photo(id_photo);

-- Insert to test
INSERT INTO Compte(login_compte, password_compte, role_compte, points_compte) VALUES 
('toto', 'password', 'admin', 0),
('babar', 'password2', 'team', 0),
('elephant', 'password3', 'coucou', 0); 