import pandas as pd
from utils.connect_to_account import connect

def scrape_post_info(max_posts):
    posts = connect(account_name = 'dreamartslndn')

    i = 0
    posts_list = []

    print('Collating post stats')
    for post in posts:
        if i == max_posts:
            break
        posts_list.append([post.date_utc, post.likes, post.comments, post.is_video, post.video_view_count])
        i+=1
    
    print('Creating data frame')
    df = pd.DataFrame(posts_list)
    
    return df