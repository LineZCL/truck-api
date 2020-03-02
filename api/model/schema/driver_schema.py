from marshmallow import Schema, fields, pre_load, validate

from flask_marshmallow import Marshmallow

ma = Marshmallow()

class DriverSchema(ma.Schema):
    id = fields.Integer() 
    name = fields.Str(required = True, error_messages = {"required": {"message": "Name is required", "code": 400}})
    age = fields.Integer()
    own_vehicle = fields.Boolean(required = True, error_messages = {"required": {"message": "Own vehicle field is required", "code": 400}})
    genre = fields.Str()
    cnh_type = fields.Str() 
    vehicle_type_id = fields.Integer(required = True, error_messages = {"required": {"message": "Vehycle type is required", "code": 400}})
    is_active = fields.Boolean() 