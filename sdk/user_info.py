from endpoints import links
from sdk.helpers import send_request, get_value_by_id, get_value_by_name, get_text_from_element
from sdk.errors import HtmlValueNotFound


class User:

    def _extract_phones(self):
        phone = get_value_by_id(self.ans.text, 'telephone1', 'input')
        phone_2 = get_value_by_id(self.ans.text, 'telephone2', 'input')
        return phone, phone_2

    def _extract_postcode(self):
        return get_value_by_name(self.ans.text, 'postcode', 'input')

    def _extract_alias(self):
        return get_value_by_name(self.ans.text, 'alias', 'input')

    def _extract_names(self):
        f = get_value_by_name(self.ans.text, 'first_name', 'input')
        l = get_value_by_name(self.ans.text, 'last_name', 'input')
        return f, l

    def update_info(self, new_data):
        '''
        Update the user data. The new_data struct should be like this:
        new_data = {
            alias: alias
            first_name: string,
            last_name: string,
            telephone1: string,
            telephone2: string,
            country_code: gr,
            postcode: string
        }
        :param new_data: Dict with specific data
        :return: msg from request
        '''
        ans = send_request('POST', url=links.control_panel, body=new_data)
        try:
            success = get_text_from_element(ans.text, 'flash', 'div', 'id')
            return success
        except HtmlValueNotFound:
            error = get_text_from_element(ans.text, 'error-message', 'span', 'class')
            return error

    def get_personal_info(self):
        return {
            'alias': self.alias,
            'telephone1': self.telephone1,
            'telephone2': self.telephone2,
            'first_name': self.f_name,
            'last_name': self.l_name,
            'postcode': self.postcode
        }

    def __init__(self):
        self.ans = send_request('GET', links.control_panel)
        self.alias = self._extract_alias()
        self.telephone1, self.telephone2 = self._extract_phones()
        self.postcode = self._extract_postcode()
        self.f_name, self.l_name = self._extract_names()
