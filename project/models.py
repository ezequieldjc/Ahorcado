from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, ForeignKey, Integer, String, Time, Date, DateTime
from sqlalchemy.sql import func
from datetime import timedelta, datetime
import random


db = SQLAlchemy()

class Jugadas(db.Model):
    __tablename__ = 'jugadas'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    puntaje = db.Column(db.Integer)
    fecha = Column(DateTime(timezone=True), nullable=False, default=func.now()+ timedelta(hours=-3))

class Universo(db.Model):
    __tablename__ = 'universo'
    id = db.Column(db.Integer, primary_key=True)
    palabra = db.Column(db.String(30))
    dificultad = db.Column(db.Integer)
