# load libraries
import toml
from utils.scrape_posts import scrape_post_info
from utils.format_table import format_output_table
from utils.save_output import save_output

# read in parameters
with open('config.toml', 'r') as f:
    config = toml.load(f)

account_name = config['account_name']
post_year = config['post_year']
max_posts = config['max_posts']
output_path = config['output_path']

# scrape post info
df = scrape_post_info(max_posts)

# format for output
df = format_output_table(df, post_year)

# save out as csv file
save_output(df, file_path = output_path)