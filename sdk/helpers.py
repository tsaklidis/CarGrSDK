from bs4 import BeautifulSoup
import requests

import settings
from sdk.errors import *


def send_request(method, url, extra_headers=None, params=None,
                 body=None, return_json=False, convert_to_json=True):

    s = requests.Session()
    final_headers = settings.main_hdrs

    if extra_headers:
        final_headers.update(extra_headers)

    if method == 'GET':
        ans = s.get(url, params=params, headers=final_headers, cookies=settings.cookies)
    elif method == 'POST':
        ans = s.post(url, data=body, cookies=settings.cookies)
    # elif method == 'DELETE':
    #     ans = requests.delete(url, data=body, headers=final_headers)
    # elif method == 'PATCH':
    #     ans = requests.patch(url, data=body, headers=final_headers)
    # elif method == 'PUT':
    #     ans = requests.put(url, data=body, headers=final_headers)
    else:
        raise Exception('Bad request type')

    return ans

def get_value_by_id(html, id, html_tag):
    soup = BeautifulSoup(html, "html.parser")
    try:
        return soup.find(html_tag, {'id': id}).get('value')
    except:
        raise HtmlValueNotFound(f'Value not found, id used {id}')

def get_value_by_name(html, name):
    pass