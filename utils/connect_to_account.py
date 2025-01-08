import instaloader

def connect(account_name):
    user = account_name
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, user)
    posts = profile.get_posts()

    return posts