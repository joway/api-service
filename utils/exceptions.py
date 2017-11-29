class BaseException(Exception):
    pass


class RoleNotFound(BaseException):
    pass


class UserNotFound(BaseException):
    pass


class PolicyFormatError(BaseException):
    pass
