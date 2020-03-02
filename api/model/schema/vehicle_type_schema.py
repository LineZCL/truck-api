from api import ma
from marshmallow import Schema, fields, pre_load, validate

class VehicleTypeSchema(ma.Schema):
    id = fields.Integer() 
    name = fields.Str(required = True, error_messages = "required": {"message": "Name is required", "code": 400})
    