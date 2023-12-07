from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import SECRET_KEY, DATABASE_URI

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.secret_key = SECRET_KEY

    app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI

    db.init_app(app)

    with app.app_context():
        from app.api import api_bp
        app.register_blueprint(api_bp, url_prefix='/api')
        from app import views
    return app

app = create_app()
migrate = Migrate(app, db)


