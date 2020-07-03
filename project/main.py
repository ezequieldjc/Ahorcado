from flask import Blueprint, render_template, request, redirect, url_for, session
from .ahorcado import Ahorcado
from project.models import db, Jugadas
from sqlalchemy import desc
import random
import string


main = Blueprint('main', __name__)
a = Ahorcado()

playhtml = "play.html"

@main.route('/')
def home():
    session.clear()
    return render_template("home.html")

@main.route('/about', strict_slashes=False)
def about():
    session.clear()
    return render_template("about.html")

@main.route('/play', strict_slashes=False)
def play():
    session.clear()
    a.limpiar_variables_total
    return render_template("play.html")

@main.route('/play/alias', methods=['POST'])
def play_alias():
    #a.limpiar_variables_total
    #name = request.form.get('name')
    #a.ingresa_alias(name)
    session.clear()
    session["user"] = request.form.get('name')
    session["puntaje"] = 0
    session["letrasing"] = ''
    session["intentos"] = 5
    return render_template(playhtml, alias=session["user"])

@main.route('/play/dificultad', methods=['POST'])
def play_dificultad():
    dif = request.form.get('dif')
    if not dif:
        dif = 1
    session["dificultad"] = a.carga_dificultad(dif)
    session["palabra"] = a.carga_universo()
    session["intentos"] = 6 - a.dificultad
    session["largo"] = a.largo_palabra(session["palabra"])
    #session["palabra"] = a.elegir_palabra()
    session["guia"] = a.crea_guia(session["palabra"])
    session["guiaM"] = a.muestra_guia(session["guia"])
    return render_template(playhtml, dificultad=session["dificultad"],alias=session["user"], intentos = session["intentos"], palabra = session["palabra"], largo = session["largo"], guia = session["guia"])

@main.route('/play/ing', methods=['POST'])
def play_ingreso():
    session["ing"] = request.form.get('ingreso')
    if len(session["ing"]) > 1:
        if session["ing"].upper() == session["palabra"]:
            session["puntaje"] = a.dev_puntaje(8)
            a.limpiar_variables_parcial()
        else:
            print(session["intentos"])
            session["intentos"] = 0
            session["puntaje"] = a.dev_puntaje(0)
    else:
        a.ingresa_letra(session["ing"].upper())
        if session["palabra"] == session["guia"]:
            session["puntaje"] = a.dev_puntaje(session["intentos"]) 
            a.limpiar_variables_parcial()
    return render_template(playhtml, puntaje = session["puntaje"], letra = session["ing"], dificultad=session["dificultad"],alias=session["user"], intentos =session["intentos"], palabra = session["palabra"], largo = session["largo"], guia = session["guia"], leting = session["letrasing"])

@main.route('/rank')
def rank():
    session.clear()
    rank=Jugadas.query.order_by(desc(Jugadas.puntaje)).limit(10).all()
    partidas = []
    date_str = ''
    c = 1
    for i in rank:
        date_str = i.fecha.strftime('%d/%m/%Y, %H:%M')
        partidas.append([c,i.nombre, i.puntaje, date_str])
        c=c+1
    return render_template("Ranking.html", partidas=partidas)

@main.route('/play/rank')
def alta_rank():
    rank=Jugadas.query.order_by(desc(Jugadas.puntaje)).limit(10).all()
    partidas = []
    date_str = ''
    c = 1
    for i in rank:
        date_str = i.fecha.strftime('%d/%m/%Y, %H:%M')
        partidas.append([c,i.nombre, i.puntaje, date_str])
        if c < 10:
            c=c+1
    new_jugada= Jugadas(nombre=session["user"], puntaje= session["puntaje"] )
    session.clear()
    db.session.add(new_jugada)
    db.session.commit()
    return render_template("Ranking.html", partidas=partidas)
    