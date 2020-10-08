class BaseException(Exception):
    message = None

    def __init__(self, message=None):
        self.message = message or self.message

    def __str__(self):
        return self.message or ''


class NotConfigured(BaseException):
    message = 'SDK is not configured'

    def __init__(self, *args, **kwargs):
        super(NotConfigured, self).__init__(*args, **kwargs)


class LoginFailed(BaseException):
    message = 'Login Failed, check your credentials'

    def __init__(self, *args, **kwargs):
        super(LoginFailed, self).__init__(*args, **kwargs)

class HtmlValueNotFound(BaseException):
    message = 'The value you requested was not found'

    def __init__(self, *args, **kwargs):
        super(HtmlValueNotFound, self).__init__(*args, **kwargs)