from flask import Blueprint
from flask_restful import Api 

blueprint = Blueprint('api', __name__, '/api')
api = Api(blueprint) 

#Routes
