from flask import Blueprint, render_template, request, redirect, url_for
main = Blueprint('main', __name__)
from .Ahorcado import Ahorcado

a = Ahorcado()

@main.route('/test')
def test():
    return "Home Page"

@main.route('/test/about/')
def about_test():
    return "About Page"

# Routes to Render Something
@main.route('/')
def home():
    return render_template("home.html")

@main.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@main.route('/play', strict_slashes=False)
def play():
    return render_template("play.html")


@main.route('/play/alias', methods=['POST'])
def play_alias():
    name = request.form.get('name')
    a.ingresa_alias(name)
    a.carga_universo()
    return render_template("play.html", alias=a.alias)