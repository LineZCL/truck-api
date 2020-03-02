from api.model.terminal import Terminal

class TerminalService: 
    def get_by_id(self, id):
        return Terminal.query.get(id)