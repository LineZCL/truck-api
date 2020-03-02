from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
db = SQLAlchemy(app)
from api.api import blueprint
app.register_blueprint(blueprint, url_prefix = '/api')

