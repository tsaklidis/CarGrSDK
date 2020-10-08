from auth import Authentication
from . user_info import User

class CarGrSDK:

    def __init__(self):
        self.auth = Authentication()
        self.user = User()

