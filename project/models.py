from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date

db = SQLAlchemy()

class Ahorcado(db.Model):
    __tablename__ = 'ahorcado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    dni = db.Column(db.String(8))
    telefono = db.Column(db.String(10))

class UniversoFacil(db.Model):
    __tablename__ = 'universoFacil'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(30))


class UniversoMedio(db.Model):
    __tablename__ = 'universoMedio'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(30))


class UniversoDificil(db.Model):
    __tablename__ = 'universoDificil'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(30))


