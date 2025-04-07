from flask import Flask
from app.config.settings import Config
from app.models import init_app as init_db
from app.routes import init_app as init_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_db(app)
    init_routes(app)  # Asegúrate que esta línea esté aquí
    return app
