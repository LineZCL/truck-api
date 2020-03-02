from flask import Blueprint
from flask_restful import Api 
from .resources.drive_resource import DriverResource

blueprint = Blueprint('api', __name__)
api = Api(blueprint) 

#Routes
api.add_resource(DriverResource, "/driver")
