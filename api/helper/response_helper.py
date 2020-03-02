from enum import Enum

class ResponseHelper:
    status = None
    message = ''
    object = None
    def __init__(self, status, message = None, object = None): 
        self.status = status
        self.message = message 
        self.object = object
    def getHttpResponse(self):
        return {'status': self.status.name, 'message': self.message, 'data': self.object } 

class Status(Enum): 
    success = 1 
    error = 2

class HttpStatus(Enum): 
    success = 200, 
    server_error = 500, 
    client_error = 400, 
    unprocessable_entity = 422