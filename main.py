import instaloader

username = input("username?\n")
password = input("password?\n")

def get_followers_list(username,password):
    L = instaloader.Instaloader()
    L.login(username,password)
    profile = instaloader.Profile.from_username(L.context, "prada")
    follower_list = []
    follower_count = 0
    for follower in profile.get_followers():
        follower_list.append(follower.username)
        follower_count += 1
    print(f"you have {follower_count} followers")
    return follower_list
