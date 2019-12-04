import argparse
import os
import praw
import urllib

reddit = praw.Reddit(client_id='CLIENT_ID', client_secret=CLIENT_SECRET', user_agent='APP_NAME', username='USERNAME', password='PASSWORD')

DOWNLOADS_DIR = 'subreddit-pictures/'

parser = argparse.ArgumentParser()

parser.add_argument('subreddit', help='The subreddit from which you wish to download the pictures', action='store')
parser.add_argument('-l', '--limit', default=15, help='Limit the number of posts to download (default: 15)', type=int, action='store')
parser.add_argument('-p', '--period', default='day', help='The period from when to download the pictures (default: day) -- options: day, month, year, all', action='store')

args=parser.parse_args()

hot_subreddit = reddit.subreddit(args.subreddit).top(args.period, limit=args.limit)

url = [post.url for post in hot_subreddit]

def download_pictures():
    for value in url:
        name = os.path.basename(value) # taking only the value after '/' from the url as name
        os.makedirs(os.path.dirname(DOWNLOADS_DIR), exist_ok=True) # creates the directory where the photos are saved if it doesn't exist
        filename = os.path.join(DOWNLOADS_DIR, name) # combine the name and the downloads directory to get the local filename
        if not os.path.isfile(filename):
            urllib.request.urlretrieve(value, filename) # if the file doesn't exist, it gets downloaded
download_pictures()
