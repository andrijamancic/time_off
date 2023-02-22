class RequestDateExceptionCode(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class RequestDateNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class WrongSuperiorException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class NoDaysException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class RequestDateAlreadyApprovedException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
