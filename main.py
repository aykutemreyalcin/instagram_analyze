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

def get_followees_list(username,password):
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, "prada")
    followees_list = []
    followees_count = 0
    for followee in profile.get_followees():
        followees_list.append(followee.username)
        followees_count += 1
    print(f"you follow {followees_count} accounts")
    return followees_list

choice = int(input("\n press 1 to see the accounts that you follow which dont follow you \n press 2 to see the accounts that follows you but you dont follow them"))

if choice == 1:
    final_list = []
    for i in get_followees_list(username,password):
        if i not in get_followers_list(username,password):
            final_list.append(i)
    for i in final_list:
        print(i)
    print(f"{len(final_list)} accounts in total")

if choice == 2:
    final_list = []
    for i in get_followers_list(username,password):
        if i not in get_followees_list(username,password):
            final_list.append(i)
    for i in final_list:
        print(i)
    print(f"{len(final_list)} accounts in total")


