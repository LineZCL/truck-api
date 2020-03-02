from flask import request
from flask_restful import Resource
from api.service.route_service import RouteService 
from api.helper.response_helper import ResponseHelper, Status, HttpStatus

class RouteCheckoutResource(Resource): 
    def put(self, id): 
        response = RouteService().checkout(id) 
        print(response)
        if response and response.status == Status.error:
            return response.getHttpResponse(), HttpStatus.not_found.value 
        print(HttpStatus.success.value)
        return ResponseHelper(Status.success).getHttpResponse()