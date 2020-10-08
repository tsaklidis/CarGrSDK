import settings

from sdk import errors
from sdk.helpers import send_request

from endpoints import links


class Authentication:
    credentials = None

    def login(self):
        '''
        Perform login and keep the cookies for further requests
        :param auth: dict with keys: username, password
        :return: request object
        '''
        res = send_request('POST', links.login_url, body=settings.credentials)
        settings.cookies = dict(res.cookies)
        if res.text == 'gotonext:/user/':
            return res
        raise errors.LoginFailed()


    def __init__(self):
        try:
            self.credentials = settings.credentials
            self.login()
        except AttributeError:
            raise errors.NotConfigured('Credentials not provided at '
                                       'settings/local.py')
