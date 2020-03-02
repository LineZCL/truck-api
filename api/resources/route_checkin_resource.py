from flask import request
from flask_restful import Resource
from api.service.route_service import RouteService 
from api.helper.response_helper import ResponseHelper, Status, HttpStatus

class RouteCheckinResource(Resource): 
    def post(self): 
        json_data = request.get_json(force = True)
        if not json_data: 
            return ResponseHelper(Status.error, message = "No Input data").getHttpResponse(), HttpStatus.client_error.value
        response = RouteService().checkin(json_data) 
        if response.status == Status.error:
            return response.getHttpResponse(), HttpStatus.unprocessable_entity.value 
        print(HttpStatus.success.value)
        return response.getHttpResponse()