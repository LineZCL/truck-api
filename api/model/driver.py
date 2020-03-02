from api import db
from enum import Enum

class Driver(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer) 
    own_vehicle = db.Column(db.Boolean, nullable = False)
    genre = db.Column(db.String(10))
    cnh_type = db.Column(db.String(1))
    vehicle_type_id = db.Column(db.Integer) 
    is_active = db.Column(db.Boolean, nullable = False, default = True)

    vehicle_types = {
        1: 'Caminhão 3/4',
        2: 'Caminhão Toco', 
        3: 'Caminhão Truck', 
        4: 'Carreta Simples',
        5: "Carreta Eixo Extendido"
    }

    def insert_or_update(self):
        if self.id is None:
            db.session.add(self) 
        db.session.commit()
    
    def inative(self): 
        is_active = False
        db.session.commit()

    def mappingJsonToModel(self, json, isCreate = True):
        self.id = json["id"] if "id" in json else None 
        self.name = json["name"] if "name" in json else None 
        self.age = json["age"] if "age" in json else None 
        self.own_vehicle = json["own_vehicle"] if "own_vehicle" in json else None 
        self.genre = self.own_vehicle = json["genre"] if "genre" in json else None 
        self.cnh_type = self.own_vehicle = json["cnh_type"] if "cnh_type" in json else None 
        self.vehicle_type_id = self.own_vehicle = json["vehicle_type_id"] if "vehicle_type_id" in json else None 
    
db.create_all()