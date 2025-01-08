import instaloader

def connect(account_name):
    user = account_name
    
    print('Connecting to account')
    loader = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(loader.context, user)

    print('Scraping post information')
    posts = profile.get_posts()

    return posts