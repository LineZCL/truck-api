from flask import request
from flask_restful import Resource
from api.service.driver_service import DriverService 
from api.helper.response_helper import ResponseHelper, Status, HttpStatus

class DriverResource(Resource):
    def post(self): 
        json_data = request.get_json(force = True)
        if not json_data: 
            return ResponseHelper(Status.error, message = "No Input data").getHttpResponse(), HttpStatus.client_error.value
        
        response = DriverService().save_driver(json_data) 
        
        if response.status == Status.error:
            return response.getHttpResponse(), HttpStatus.unprocessable_entity.value 
        print(HttpStatus.success.value)
        return response.getHttpResponse()

    def put(self): 
        json_data = request.get_json(force = True)
        if not json_data: 
            return ResponseHelper(Status.error, message = "No Input data").getHttpResponse(), HttpStatus.client_error.value
        response = DriverService().save_driver(json_data) 
        
        if response.status == Status.error:
            return response.getHttpResponse(), HttpStatus.unprocessable_entity.value 
        print(HttpStatus.success.value)
        return response.getHttpResponse()
