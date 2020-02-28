from api import db

class VehicleType(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), unique = True, nullable = False)

    def insert_or_update(self):
        if self.id is None:
            db.session.add(self) 
        db.session.commit()
    
    def vehycles_type_seeder():
        vehycles_type = VehicleType.query.all() 
        if not vehycles_type:
            trucks_types_name = ['Caminhão 3/4', 'Caminhão Toco', 'Caminhão Truck', 'Carreta Simples', "Carreta Eixo Extendido"]
            for truck in trucks_types_name:
                VehicleType(name = truck).insert_or_update()


db.create_all()
VehicleType.vehycles_type_seeder()