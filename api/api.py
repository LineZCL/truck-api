from flask import Blueprint
from flask_restful import Api 
from .resources.drive_resource import DriverResource
from api.resources.route_checkin_resource import RouteCheckinResource
from api.resources.route_checkout_resource import RouteCheckoutResource

blueprint = Blueprint('api', __name__)
api = Api(blueprint) 

#Routes
api.add_resource(DriverResource, "/driver")
api.add_resource(RouteCheckinResource, "/route/checkin")
api.add_resource(RouteCheckoutResource, "/route/checkout/<int:id>")
