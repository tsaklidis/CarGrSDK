import json

from sdk.helpers import refresh_item


class CustomItem:
    title = None
    id = None

    def refresh(self):
        return refresh_item(self.id)

    def __init__(self, data):
        self.title = data.get('title')
        self.id = data.get('id')

    def __str__(self):
        return '<CustomItem() obj> {}'.format(self.title)

    def __repr__(self):
        return '<CustomItem() obj> {}'.format(self.title)