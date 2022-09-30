import requests
import json
import os
#github username : @anuragd275
#Welcome message
welcome_message = "=======================Welcome to GitHub Profile Accessor=======================\nPlease enter GitHub username to access GitHub Profile"
print(welcome_message)

#API URL
api_url = "https://api.github.com/users/" 
username = input("Enter username : ")


# API in action
responce = requests.get(api_url + f"{username}")
data = json.loads(responce.text)

#accessing image object
img = requests.get(data["avatar_url"])

#WRITE/LOAD CONTENT ON FILE
fp = open("{}.png".format(username), "wb") 
fp.write(img.content)
fp.close()
print("Downloaded {}'s Successfully.".format(username))
