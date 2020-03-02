from api.model.route import Route
from api.model.schema.route_schema import RouteSchema 
from api.helper.response_helper import ResponseHelper, Status
from marshmallow import ValidationError 
from datetime import datetime
class RouteService: 
    def checkin(self, json_data): 
        route_schema = RouteSchema() 
        data, errors = route_schema.load(json_data) 
        if errors : 
            return ResponseHelper(Status.error, message = errors)
        
        route = Route()
        route.mapping_json_to_model(json_data)

        route.departure_time = datetime.now()
        route.insert_or_update()

        return ResponseHelper(Status.success, object = route_schema.dump(route).data) 
    def checkout (self, id): 
        route = Route.query.get(id) 
        
        if not route: 
            return ResponseHelper(Status.error, message = "Route not found" )
         
        route.arrive_time = datetime.now()
        route.is_active = False 
        route.insert_or_update()


