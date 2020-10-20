import json
import os
import settings

from sdk import errors
from sdk.helpers import send_request, get_text_from_element

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

    def _validate_cookie(self, html_to_check):
        '''
        When the user is logged in, there is the name on the top panel
        :param html: Any html of the site
        :return: None if user is not logged in
        '''

        return get_text_from_element(html_to_check, 'thename', 'span', 'class')

    def _remove_cookies(self):
        the_file = os.path.dirname(os.path.abspath(__file__)) + '/cookie.json'
        if os.path.exists(the_file):
            os.remove(the_file)
            settings.cookies = ''


    def _save_cookie(self, cookie):
        cookie = dict(cookie)
        the_file = os.path.dirname(os.path.abspath(__file__)) + '/cookie.json'
        settings.cookies = cookie
        with open(the_file, 'w+') as outfile:
            json.dump({'cookies': cookie}, outfile)

    def _load_cookie(self):
        the_file = os.path.dirname(os.path.abspath(__file__)) + '/cookie.json'
        if os.path.exists(the_file):
            with open(the_file) as outfile:
                data = json.load(outfile)
                try:
                    cookies = data.get('cookies')
                    # Make a request to a protected area in order to check if
                    # site accepts the saved cookie
                    ans = send_request('GET', 'https://www.car.gr/',
                                       cookies=cookies)
                    if self._validate_cookie(ans.text):
                        settings.cookies = cookies
                        return True
                    else:
                        self._remove_cookies()
                        return False
                except Exception as e:
                    raise errors.CookieError()
        return None

    def login(self):
        '''
        Perform login and keep the cookies for further requests
        :param auth: dict with keys: username, password
        :return: request object
        '''
        if self._load_cookie():
            return True
        else:
            res = send_request('POST', links.login_url, body=settings.credentials)
            self._save_cookie(res.cookies)
            if res.text == 'gotonext:/user/':
                return res
            else:
                errors.LoginFailed()


    def __init__(self):
        self.check_credentials()
        self.login()
