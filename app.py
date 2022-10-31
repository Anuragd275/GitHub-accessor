import requests

username = input("Enter GitHub username : ")
url = "https://api.github.com/users/{}".format(username)

response = requests.get(url)
data = response.json()

details = []


def user_details(username):
    name = ("Name : {}".format(data['name']))
    details.append(name)  # ? append function has to be used multiple times
    user_name = ("Username : {}".format(data['login']))
    details.append(user_name)
    bio = ("bio : {}".format(data['bio']))
    details.append(bio)
    company = ("Company : {}".format(data['company']))
    details.append(company)
    website = ("website : {}".format(data['blog']))
    details.append(website)
    location = ("location : {}".format(data['location']))
    details.append(location)
    twitter = ("twitter : {}".format(data['twitter_username']))
    details.append(twitter)
    followers = ("Followers : {}".format(data['followers']))
    details.append(followers)
    following = ("Following : {}".format(data['following']))
    details.append(following)
    repos = ("Public Repositories : {}".format(data['public_repos']))
    details.append(repos)

    print("Wrote {}'s details successfully.".format(username))


def users_dp(username):
    user_dp = requests.get(data['avatar_url'])
    fp = open("{}.png".format(username), "wb")
    fp.write(user_dp.content)
    fp.close()
    print("Downloaded {}'s successfully.".format(username))


user_details(username)
users_dp(username)


with open(r'{}.txt'.format(username), 'w') as fp:
    fp.write('\n'.join(details))


n = input("press Y to run the program again \n press any key to exit the program")

