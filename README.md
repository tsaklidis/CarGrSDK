### Car.gr SDK
#### This is an experiment for automations on car.gr site
##### Working on free time so... follow for new updates
<hr>

Automate some functionalities. Some of them are:
<ul>
    <li>Update all user ads</li>
    <li>Update specific user ads</li>
    <li>Get user info</li>
    <li>Update specific fields on user profile</li>
    <li>Get user's ads in objects</li>
    <li>Get user's ads (titles only)</li>
</ul>
<hr>

#### How to use:
<ol>
    <li>Create a file named local.py under the settings folder. The file should be based on <strong>local.py.example</strong></li>
    <li>Fill your username and password. The credentials are not saved, the are just forwarded to the site (you can check the source code)</li>
    <li>Initialize the sdk in your script and you are ready to go</li>
    <li>The folder <a href="examples">examples</a> has some basic steps</li>
</ol>

```python
# Initialize
client = CarGrSDK()

# Get user ads
ads = client.user.get_ads()

# Update all available ads
for ad in ads:
    ad.refresh()
```

#### Full Documentation:
The full documentation and complete functionalities are described at <a href="documentation.md">documentation.md</a> file

<hr>

#### TODO:
<ul>
    <li>Create new listing</li>
    <li>Delete specific listing</li>
    <li>Delete all listing</li>
</ul>
