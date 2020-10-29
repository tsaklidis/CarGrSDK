from sdk.base import CarGrSDK

# Initialize the SDK
# The sdk will automatically try to log you in based on the credentials you
# provided at settings/local.py
client = CarGrSDK()

# Get the logged in user data
info = client.user.get_personal_info()
print(info)

# Update user info
info['first_name'] = 'Stefanos'
info['country_code'] = 'gr'

ans = client.user.update_info(info)
print(ans)

# Get user ads
ads = client.user.get_ads()
print(ads)

# Update all available ads
for ad in ads:
    # Update the item
    result = ad.refresh()
    # View results
    print(f'Item: {ad.title} result: {result}')
