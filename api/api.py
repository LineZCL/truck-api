from flask import Blueprint
from flask_restful import Api 
from .resources.driver_resource import DriverResource
from .resources.driver_own_vehicle_resource import DriverOwnVehicleResource
from .resources.driver_no_charge_resource import DriverNoChargeResource
from api.resources.route_checkin_resource import RouteCheckinResource
from api.resources.route_checkout_resource import RouteCheckoutResource


blueprint = Blueprint('api', __name__)
api = Api(blueprint) 

#Routes
api.add_resource(DriverResource, "/driver")
api.add_resource(DriverOwnVehicleResource, "/driver/own-vehicle")
api.add_resource(DriverNoChargeResource, "/driver/no-charge")
api.add_resource(RouteCheckinResource, "/route/checkin")
api.add_resource(RouteCheckoutResource, "/route/checkout/<int:id>")
