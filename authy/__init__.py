__version_info__ = ('1', '1', '0')
__version__ = '.'.join(__version_info__)


class AuthyException(Exception):
    pass


class AuthyApiException(AuthyException):

    def __init__(self, status, uri, msg=""):
        self.uri = uri
        self.status = status
        self.msg = msg

    def __str__(self):
        return "HTTP ERROR %s: %s \n %s" % (self.status, self.msg, self.uri)

