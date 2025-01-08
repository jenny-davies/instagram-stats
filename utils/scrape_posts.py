import pandas as pd

def scrape_post_info(max_posts):
    i = 0
    posts_list = []

    for post in posts:
        if i == max_posts:
            break
        posts_list.append([post.date_utc, post.likes, post.comments, post.is_video, post.video_view_count])
        i+=1
    
    df = pd.DataFrame(posts_list)
    
    return df