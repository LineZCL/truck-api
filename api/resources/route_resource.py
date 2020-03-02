from flask import request
from flask_restful import Resource
from api.service.route_service import RouteService 
from api.helper.response_helper import ResponseHelper, Status, HttpStatus

class RouteResource(Resource): 
    def get(self): 
        routes = RouteService().get_routes_actives() 
        if routes:
            return ResponseHelper(Status.success, object= routes).getHttpResponse()
        return ResponseHelper(Status.success).getHttpResponse()