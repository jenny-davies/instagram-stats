import datetime
from utils.scrape_posts import scrape_post_info

def format_output_table(post_year):
    df = scrape_post_info(max_posts = 60)
    
    print('Formatting output table')
    # name columns
    df.columns = ['timestamp', 'n_likes', 'n_comments', 'video', 'video_views']

    # filter for year
    df = df[df['timestamp'].astype(str).str[0:4] == post_year].reset_index(drop = True)

    # derive additional columns
    df['weekday'] = df['timestamp'].dt.day_name()
    df['hour_posted'] = df['hour_posted'].dt.hour
    df['hour_posted'] = df['hour_posted'].apply(lambda x: str(x - 12)+'pm' if x > 12 else str(x)+'am')

    return df