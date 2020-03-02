
from api import app
 
#import models 
from api.model.terminal import Terminal
from api.model.driver import Driver
from api.model.route import Route

if __name__ == '__main__': 
    app.run(debug = True)

    

