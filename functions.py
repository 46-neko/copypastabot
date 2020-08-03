import requests
import praw

reddit = praw.Reddit(client_id = "your_client_id",
                    client_secret = "your_client_secret",
                    user_agent="your_user_agent")

def help_response(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = "/randomcopypasta = Shows a random copypasta\n/randomemojipasta = Shows a random emojipasta\nOBS: If the bot doesn't send anything, please try again. If the random thread's selftext is either an image or a link, the bot won't send the message, that's not a bug.")

def start_response(update, context):
    context.bot.send_message(chat_id = update.message.chat_id, text = "Welcome to the Copypasta Bot. Type ''/help'' to see the commands.")

def randomcopypasta_response(update, context):
    submission = reddit.subreddit("copypasta").random()
    context.bot.send_message(chat_id = update.message.chat_id, text = submission.selftext)

def randomemojipasta_response(update, context):
    submission = reddit.subreddit("emojipasta").random()
    context.bot.send_message(chat_id = update.message.chat_id, text = submission.selftext)
