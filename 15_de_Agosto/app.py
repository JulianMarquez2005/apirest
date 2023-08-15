from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app= Flask (__name__)

#configuracion de la base de datos#

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Tonita2005"
app.config['MYSQL_DB'] = "flask_sqlalchemy"
app.config['MYSQL_PORT'] = 3307

FULL_URL_DB = f"mysql://{app.config['MYSQL_USER']}:{app.config['MYSQL_PASSWORD']}@{app.config['MYSQL_HOST']}:{app.config['MYSQL_PORT']}/{app.config['MYSQL_DB']}"


app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#Configuracion de la migracion#

migrate = Migrate()
migrate.init_app(app, db)

#Escribimos la clase que se quiere mapear#

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(250))
    apellido = db.Column(db.String(250))
    correo = db.Column(db.String(250))

    def __init__(self, id, nombre, apellido, correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

    def json(self):
        return {'id': self.id, 'nombre': self.nombre, 'apellido': self.apellido, 'correo': self.correo}

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)