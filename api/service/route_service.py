from api.model.route import Route
from api.model.schema.route_schema import RouteSchema 
from api.helper.response_helper import ResponseHelper, Status
from marshmallow import ValidationError 
from datetime import datetime
from api.service.driver_service import DriverService
from api.service.terminal_service import TerminalService
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
        
    def create_driver_routes(self, driver, origin, destiny):
        return {'driver': driver.name, 'origin': {'terminal': origin.name, 'longitude': origin.longitude, 'latitude': origin.latitude}, 
        'destiny': {'terminal': destiny.name, 'longitude': destiny.longitude, 'latitude': destiny.latitude}} 

    def get_routes_actives(self):
        driver_service = DriverService()
        terminal_service = TerminalService()
        routes = Route.query.filter(Route.is_active == True).all() 

        result = []
        for route in routes : 
            driver = driver_service.get_driver_by_id(route.driver_id)
            origin = terminal_service.get_by_id(route.origin_id)
            destiny = terminal_service.get_by_id(route.destiny_id)
            result.append(self.create_driver_routes(driver, origin, destiny))

        return result