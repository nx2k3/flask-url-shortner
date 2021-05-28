from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("settings.py")
    db.init_app(app)
    from .views import short
    app.register_blueprint(short)
    return app

