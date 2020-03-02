from api import ma
from marshmallow import Schema, fields, pre_load, validate

class RouteSchema(ma.Schema):
    id = fields.Integer() 
    departure_time = fields.DateTime()
    arrive_time = fields.DateTime()
    is_loaded = fields.Boolean(required = True, error_messages = "required": {"message": "Is loadead field is required", "code": 400})
    origin_id =  fields.Integer(required = True, error_messages = "required": {"message": "Origin Id field is required", "code": 400})
    destiny_id =  fields.Integer(required = True, error_messages = "required": {"message": "Destiny id field is required", "code": 400})
    driver_id =  fields.Integer(required = True, error_messages = "required": {"message": "Driver id field is required", "code": 400})
    is_active = fields.Boolean() 