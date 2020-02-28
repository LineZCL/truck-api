from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/truck.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)


db.create_all()