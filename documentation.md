#### class User:
Here we assume the client is an instance of CarGrSDK()

**client.get_personal_info()**
- Used for: Getting personal info of the logged in user
- Accepts: -
- Returns: Python dict with the available values
- Example: examples/basic.py
- Notes: -


**client.get_ads()**
- Used for: Getting all the ads of the user
- Accepts: -
- Returns: Python list with CustomItem() objects
- Example: examples/basic.py
- Notes: -

<hr>

#### class CustomItem:
Here we assume the ad is an instance of the CustomItem class

**ad.refresh()**
- Used for: Refreshes the ad, bring to the top of the car.gr list. 
- Accepts: -
- Returns: Python dict with message about the action.
- Example: examples/basic.py
- Notes: There are limits from car.gr about the times you can update an ad.