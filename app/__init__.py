from flask_restful import Api
from flask import Flask, config
from flask_sqlalchemy import SQLAlchemy
from config import config
from dotenv import load_dotenv

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)

    load_dotenv()
    app.config.from_object(config[config_name])

    api = Api(app, prefix='/api/v1')
    api.init_app(app)
    
    db.init_app(app)

    from app.resources.contacts import Contacts
    api.add_resource(Contacts, '/contacts')

    return app