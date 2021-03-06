from flask import request
from flask_restful import Resource
from api.service.driver_service import DriverService 
from api.helper.response_helper import ResponseHelper, Status, HttpStatus

class DriverOwnVehicleResource(Resource): 
    def get(self): 
        drivers = DriverService().get_drivers_own_vehicle() 
        if drivers:
            print(drivers)
            return ResponseHelper(Status.success, object= drivers).getHttpResponse()
        return ResponseHelper(Status.success).getHttpResponse()