class FieldsAreEmpty(Exception):
    def __init__(self, message):
        self.message = message
        

class InvalidLeadId(Exception):
    def __init__(self, message):
        self.message = message
