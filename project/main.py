from flask import Blueprint, render_template, request, redirect, url_for
from .Ahorcado import Ahorcado
from project.models import db, Jugadas
from sqlalchemy import desc


main = Blueprint('main', __name__)
a = Ahorcado('name')

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@main.route('/play', strict_slashes=False)
def play():
    a.limpiar_variables_total
    return render_template("play.html")

@main.route('/play/alias', methods=['POST'])
def play_alias():
    a.limpiar_variables_total
    name = request.form.get('name')
    a.ingresa_alias(name)
    return render_template("play.html", alias=a.alias)

@main.route('/play/dificultad', methods=['POST'])
def play_dificultad():
    dif = request.form.get('dif')
    if not dif:
        dif = 1
    a.carga_dificultad(dif)
    a.carga_universo()
    a.intentos = 6 - a.dificultad
    a.elegir_palabra()
    a.crea_guia(a.palabra)
    a.muestra_guia(a.guia)
    return render_template("play.html", dificultad=a.dificultad,alias=a.alias, intentos = a.intentos, palabra = a.palabra, largo = a.lpalabra, guia = a.guia)

@main.route('/play/ing', methods=['POST'])
def play_ingreso():
    ing = request.form.get('ingreso')
    if len(ing) > 1:
        if ing.upper() == a.palabra:
            a.dev_puntaje(8)
            a.limpiar_variables_parcial()
        else:
            print(a.intentos)
            a.intentos = 0
            a.dev_puntaje(0)
    else:
        a.ingresa_letra(ing.upper())
        if a.palabra == a.guia:
            a.dev_puntaje(a.intentos) 
            a.limpiar_variables_parcial()
    return render_template("play.html", puntaje = a.puntaje, letra = ing, dificultad=a.dificultad,alias=a.alias, intentos = a.intentos, palabra = a.palabra, largo = a.lpalabra, guia = a.guia, leting = a.letrasing)

@main.route('/rank')
def rank():
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
def altaRank():
    new_jugada= Jugadas(nombre=a.alias, puntaje= a.puntaje )
    db.session.add(new_jugada)
    db.session.commit()
    return render_template("Ranking.html")


