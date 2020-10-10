import settings

from sdk import errors
from sdk.helpers import send_request

from endpoints import links


class Authentication:
    credentials = None

    def check_credentials(self):
        '''
        Check if user has provided and filled the credentials
        :return: None on success
        :raises: NotConfigured exception
        '''
        try:
            self.credentials = settings.credentials
            username = self.credentials.get('username')
            password = self.credentials.get('password')
            if username and password:
                return None
            else:
                raise errors.NotConfigured('Provide non empty username and '
                                           'password at settings/local.py')
        except AttributeError:
            raise errors.NotConfigured('Credentials not provided at '
                                       'settings/local.py')

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
        self.check_credentials()
        self.login()
