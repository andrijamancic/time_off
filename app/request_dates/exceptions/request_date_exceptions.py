class RequestDateExceptionCode(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class RequestDateNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
