from endpoints import links
from sdk.helpers import send_request, get_value_by_id, get_value_by_name
from sdk.errors import HtmlValueNotFound


class User:
    first_name = None
    last_name = None
    phone = None
    email = None
    post_code = None

    def _extract_phone(self, html):
        try:
            return get_value_by_id(html, 'telephone1', 'input')
        except HtmlValueNotFound:
            return None

    def _extract_postcode(self, html):
        try:
            return get_value_by_name(html, 'postcode')
        except HtmlValueNotFound:
            return None

    def __init__(self):
        ans = send_request('GET', links.control_panel)
        self.phone = self._extract_phone(ans.text)
        self.post_code = self._extract_postcode(ans.text)