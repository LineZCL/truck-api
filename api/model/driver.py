from api import db
from enum import Enum

class Driver(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer) 
    own_vehicle = db.Column(db.Boolean, nullable = False)
    genre = db.Column(db.String(10))
    cnh = db.Column(db.String(1))
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
class Genre(Enum): 
    female = 1 
    male = 2
    other = 3

class CNH(Enum): 
    A = 1
    B = 2 
    C = 3
    D = 4 
    E = 5

db.create_all()