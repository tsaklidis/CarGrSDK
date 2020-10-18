from sdk.base import CarGrSDK

# Initialize the SDK
# The sdk will automatically try to log you in based on the credentials you
# provided at settings/local.py
client = CarGrSDK()

# Get the logged in user data

info = client.user.get_personal_info()
print(info)

info['first_name'] = 'Stefanos'
info['country_code'] = 'gr'

ans = client.user.update_info(info)
print(ans)

ans = client.user.get_ads_titles()
print(ans)