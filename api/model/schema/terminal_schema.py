from marshmallow import Schema, fields, pre_load, validate
from flask_marshmallow import Marshmallow

ma = Marshmallow()
class TerminalSchema(ma.Schema):
    id = fields.Integer() 
    name = fields.Str(required = True, error_messages = {"required": {"message": "Name is required", "code": 400}})
    longitude = fields.Str(required = True, error_messages = {"required": {"message": "Longitude is required", "code": 400}})
    latitude = fields.Str(required = True, error_messages = {"required": {"message": "Latitude is required", "code": 400}})
    is_active = fields.Boolean() 
    