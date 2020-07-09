from flask import Flask , session
from .models import db

def create_app(config_name):
    app = Flask(__name__)
    app.config['WTF_CSRF_ENABLED'] = True # Sonarcloud

    app.secret_key = "1234"

    app.config['SECRET_KEY'] = 'e826016dbfecf5254f9aada20205c4448bab4d2f321c2bbca85c624640d7fb18'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://xpfghngjctzyyv:e826016dbfecf5254f9aada20205c4448bab4d2f321c2bbca85c624640d7fb18@ec2-50-16-198-4.compute-1.amazonaws.com:5432/d2ajllg55s6ehd'
    db.init_app(app)

    with app.app_context():
        db.create_all()
    

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app