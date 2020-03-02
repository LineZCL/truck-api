from flask import request
from flask_restful import Resource
from api.service.driver_service import DriverService 
from api.helper.response_helper import ResponseHelper, Status, HttpStatus

class DriverNoChargeResource(Resource): 
    def get(self): 
        drivers = DriverService().get_drivers_no_charge() 
        if drivers:
            print(drivers)
            return ResponseHelper(Status.success, object= drivers).getHttpResponse()
        return ResponseHelper(Status.success).getHttpResponse()