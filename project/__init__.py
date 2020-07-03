from flask import Flask , session
from .models import db

def create_app(config_name):
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = True # Sonarcloud

    app.secret_key = "1234"

    app.config['SECRET_KEY'] = '1eab0cc55df07f487a356cc0df610aa365d6d69aaaf1eb399da61f20104d06aa'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://qnmpruhxfeoklo:1eab0cc55df07f487a356cc0df610aa365d6d69aaaf1eb399da61f20104d06aa@ec2-52-0-155-79.compute-1.amazonaws.com:5432/d7k9i0f2ad0li0'

    db.init_app(app)

    with app.app_context():
        db.create_all()
    

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app