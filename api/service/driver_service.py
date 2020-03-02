from api.model.driver import Driver
from api.model.schema.driver_schema import DriverSchema
from api.helper.response_helper import ResponseHelper, Status
from marshmallow import ValidationError
from sqlalchemy.orm import sessionmaker
from api.model.route import Route


drivers_schema = DriverSchema(many = True)
class DriverService:

    def save_driver(self, json):

        driver_schema = DriverSchema()
        data, errors = driver_schema.load(json) 

        if errors:
            return ResponseHelper(Status.error, message = errors)
        
        driver = Driver() 
        driver.mapping_json_to_model(json) 
        driver.insert_or_update()
        return ResponseHelper(Status.success, object = driver_schema.dump(driver).data) 

    def get_drivers_own_vehicle(self):
        drivers = Driver.query.filter(Driver.own_vehicle == True).all()
        return drivers_schema.dump(drivers)
    
    def get_drivers_no_charge(self): 
        routes = Route.query.filter(Route.is_loaded == False).filter(Route.is_active == True).all()
        drivers = [] 
        
        for route in routes:
            drivers.append(Driver.query.get(route.driver_id)) 

        return drivers_schema.dump(drivers) 

        