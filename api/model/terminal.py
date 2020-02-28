from api import db

class Terminal(db.Model): 
    id = db.Column(db.Integer, primary_key = True) 
    name = db.Column(db.String(80), nullable = False, unique = True)
    longitude = db.Column(db.String(80), nullable = False)
    latitude = db.Column(db.String(80), nullable = False)
    is_active = db.Column(db.Boolean, default = True)

    def insert_or_update(self):
        if self.id is None:
            db.session.add(self) 
        db.session.commit()
    
    def inative(self): 
        is_active = False
        db.session.commit()
    
    def terminal_seeder():
        terminals = Terminal.query.all()
        if not terminals: 
            terminal = Terminal(name = 'São Paulo', latitude = '-23.602587', longitude = '-46.674354')
            terminal.insert_or_update()
            terminal2 = Terminal(name = 'Mogi', latitude = '-23.532282', longitude = '-46.199219')
            terminal2.insert_or_update()
            terminal3 = Terminal(name = 'Campinas', latitude = '-22.893333', longitude = '-47.067118')
            terminal3.insert_or_update()
            terminal4 = Terminal(name = 'Rio de Janeiro', latitude = '-22.936132', longitude = '-43.371208')
            terminal4.insert_or_update()

db.create_all() 
Terminal.terminal_seeder()
