class RequestNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmptyRequestException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class LateCancelException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code

