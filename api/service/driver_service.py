from api.model.driver import Driver
from api.model.schema.driver_schema import DriverSchema
from api.helper.response_helper import ResponseHelper, Status
from marshmallow import ValidationError

class DriverService:

    def create_driver(self, json):

        driver_schema = DriverSchema()
        data, errors = driver_schema.load(json) 

        if errors:
            return ResponseHelper(Status.error, message = errors)
        
        driver = Driver() 
        driver.mappingJsonToModel(json) 
        driver.insert_or_update()
        return ResponseHelper(Status.success, object = driver_schema.dump(driver).data) 
        