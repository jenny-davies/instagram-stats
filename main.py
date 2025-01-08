from utils.connect_to_account import connect
from utils.scrape_posts import scrape_post_info
from utils.format_table import format_output_table
from utils.save_output import save_output

connect(account_name = 'dreamartslndn')

scrape_post_info(max_posts = 60)

format_output_table(post_year = 2024)

save_output(file_path = 'instagram-stats.csv')