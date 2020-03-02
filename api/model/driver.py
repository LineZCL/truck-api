from api import db
from enum import Enum

class Driver(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer) 
    own_vehicle = db.Column(db.Boolean, nullable = False)
    genre = db.Column(db.String(10))
    cnh_type = db.Column(db.String(1))
    vehicle_type_id = db.Column(db.Integer, db.ForeignKey('vehicle_type.id'),
        nullable = False)
    vehicle_type = db.relationship('VehicleType')
    is_active = db.Column(db.Boolean, default = True)

    def insert_or_update(self):
        if self.id is None:
            db.session.add(self) 
        db.session.commit()
    
    def inative(self): 
        is_active = False
        db.session.commit()

    def mappingJsonToModel(self, json):
        self.id = None if not json["id"] else json["id"]
        self.name = json["name"]
        self.age = json["age"]
        self.own_vehicle = json["own_vehicle"] 
        self.genre = json["genre"]
        self.cnh_type = json["cnh_type"]
        self.vehicle_type_id = json["vehicle_type_id"] 
        self.is_active = json["is_active"]
    
db.create_all()