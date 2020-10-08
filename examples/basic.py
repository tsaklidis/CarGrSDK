from sdk.base import CarGrSDK

# Initialize the SDK
# The sdk will automatically try to log you in based on the credentials you
# provided at settings/local.py
client = CarGrSDK()

# Get the loged in user data
print(f'Phone: {client.user.phone}')
print(f'Post Code: {client.user.post_code}')