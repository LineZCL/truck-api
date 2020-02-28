from api import app
from api import db

# import models
from api.model.vehicle_type import VehicleType
from api.model.terminal import Terminal
from api.model.driver import Driver
from api.model.route import Route

if __name__ == '__main__':
    app.run(port = 8080, debug = True)
    