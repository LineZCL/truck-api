from api import db 

class Route(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    departure_time = db.Column(db.DateTime)
    arrive_time = db.Column(db.DateTime)
    is_loaded = db.Column(db.Boolean, nullable = False)
    origin_id =  db.Column(db.Integer, db.ForeignKey('terminal.id'),
        nullable = False)
    origin = db.relationship('Terminal')
    destiny_id =  db.Column(db.Integer, db.ForeignKey('terminal.id'),
        nullable = False)
    destiny = db.relationship('Terminal')
    driver_id =  db.Column(db.Integer, db.ForeignKey('driver.id'),
        nullable = False)
    driver = db.relationship('Driver')
    is_active = db.Column(db.Boolean, default = True)
    def insert_or_update(self):
        if self.id is None:
            db.session.add(self) 
        db.session.commit()
    
    def inative(self): 
        is_active = False
        db.session.commit()
db.create_all() 
    