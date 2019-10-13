import praw
import telegram
import requests

bot = telegram.Bot(token='Insert Bot Token Here')
reddit = praw.Reddit(client_id=' Insert client_id here', client_secret='inser client_secret here ', user_agent=' add user agent here')


def telegram_sendtext(bot_message):
    bot_token = 'Add telegram bot token'
    chat_id = " @'name of the subreddit' "
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)


posts = []

top_posts = reddit.subreddit('name of subreddit').top('day', limit=20)

for post in top_posts:
    message = post.title + '\n' + post.selftext
    telegram_sendtext(message)
