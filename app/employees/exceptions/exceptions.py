class EmployeeNotFoundException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeInvalidPasswordException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code


class EmployeeNotSuperiorException(Exception):
    def __init__(self, message, code):
        self.message = message
        self.code = code
