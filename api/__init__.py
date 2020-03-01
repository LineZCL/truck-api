from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from api.api import blueprint

app = Flask(__name__)

app.config.from_object('config')
app.register_blueprint(blueprint)
db = SQLAlchemy(app)