from flask import Blueprint, render_template, request, redirect, url_for
from .Ahorcado import Ahorcado
from project.models import db, Jugadas
from sqlalchemy import desc
import random
import string

def ran(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

main = Blueprint('main', __name__)
a = []
x = Ahorcado(ran)
a.append(x)
b = len(a)
b = b-1

@main.route('/')
def home():
    return render_template("home.html")

@main.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@main.route('/play', strict_slashes=False)
def play():
    a[b].limpiar_variables_total
    return render_template("play.html")

@main.route('/play/alias', methods=['POST'])
def play_alias():
    a[b].limpiar_variables_total
    name = request.form.get('name')
    a[b].ingresa_alias(name)
    return render_template("play.html", alias=a[b].alias)

@main.route('/play/dificultad', methods=['POST'])
def play_dificultad():
    dif = request.form.get('dif')
    if not dif:
        dif = 1
    a[b].carga_dificultad(dif)
    a[b].carga_universo()
    a[b].intentos = 6 - a[b].dificultad
    a[b].elegir_palabra()
    a[b].crea_guia(a[b].palabra)
    a[b].muestra_guia(a[b].guia)
    return render_template("play.html", dificultad=a[b].dificultad,alias=a[b].alias, intentos = a[b].intentos, palabra = a[b].palabra, largo = a[b].lpalabra, guia = a[b].guia)

@main.route('/play/ing', methods=['POST'])
def play_ingreso():
    ing = request.form.get('ingreso')
    if len(ing) > 1:
        if ing.upper() == a[b].palabra:
            a[b].dev_puntaje(8)
            a[b].limpiar_variables_parcial()
        else:
            print(a[b].intentos)
            a[b].intentos = 0
            a[b].dev_puntaje(0)
    else:
        a[b].ingresa_letra(ing.upper())
        if a[b].palabra == a[b].guia:
            a[b].dev_puntaje(a[b].intentos) 
            a[b].limpiar_variables_parcial()
    return render_template("play.html", puntaje = a[b].puntaje, letra = ing, dificultad=a[b].dificultad,alias=a[b].alias, intentos = a[b].intentos, palabra = a[b].palabra, largo = a[b].lpalabra, guia = a[b].guia, leting = a[b].letrasing)

@main.route('/rank')
def rank():
    rank=Jugadas.query.order_by(desc(Jugadas.puntaje)).limit(10).all()
    partidas = []
    date_str = ''
    c = 1
    for i in rank:
        date_str = i.fecha[b].strftime('%d/%m/%Y, %H:%M')
        partidas.append([c,i.nombre, i.puntaje, date_str])
        c=c+1
    return render_template("Ranking.html", partidas=partidas)

@main.route('/play/rank')
def altaRank():
    new_jugada= Jugadas(nombre=a[b].alias, puntaje= a[b].puntaje )
    db.session.add(new_jugada)
    db.session.commit()
    return render_template("Ranking.html")


