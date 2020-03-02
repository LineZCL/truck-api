from api import db 

class Route(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    departure_time = db.Column(db.DateTime)
    arrive_time = db.Column(db.DateTime)
    is_loaded = db.Column(db.Boolean, nullable = False)
    origin_id =  db.Column(db.Integer, db.ForeignKey('terminal.id'),
        nullable = False)
    origin = db.relationship('Terminal', foreign_keys = [origin_id])
    destiny_id =  db.Column(db.Integer, db.ForeignKey('terminal.id'),
        nullable = False)
    destiny = db.relationship('Terminal', foreign_keys = [destiny_id])
    driver_id =  db.Column(db.Integer, db.ForeignKey('driver.id'),
        nullable = False)
    driver = db.relationship('Driver', foreign_keys = [driver_id])
    is_active = db.Column(db.Boolean, default = True)
    def insert_or_update(self):
        if self.id is None:
            db.session.add(self) 
        db.session.commit()
    
    def inative(self): 
        is_active = False
        db.session.commit()

    def mapping_json_to_model(self, json):
        self.id = json["id"] if "id" in json else None 
        self.departure_time = json["departure_time"] if "departure_time" in json else None 
        self.arrive_time = json["arrive_time"] if "arrive_time" in json else None 
        self.is_loaded = json["is_loaded"] if "is_loaded" in json else None 
        self.origin_id = json["origin_id"] if "origin_id" in json else None 
        self.destiny_id = json["destiny_id"] if "destiny_id" in json else None 
        self.driver_id =  json["driver_id"] if "driver_id" in json else None 

db.create_all() 
    