"""
author: Florian Krach
"""

# ==============================================================================
# IMPORTS
import telegram
import time
import os


# ==============================================================================
# GLOBAL VARIABLES

# token for the bot:
token = None

# chat id for: Cloud-Computing-Notifiications
chat_id = None


# ==============================================================================
def send_message(bot, **kwargs):
    try:
        bot.send_message(**kwargs)
    except telegram.TelegramError as e:
        print("TELEGRAM BOT: Error while sending message:")
        print(e)
        print("wait for 35 seconds and try again")
        time.sleep(35)
        bot.send_message(**kwargs)

def send_document(bot, filename, **kwargs):
    try:
        bot.send_document(document=open(filename, 'rb'), **kwargs)
    except telegram.TelegramError as e:
        print("TELEGRAM BOT: Error while sending document:")
        print(e)
        print("wait for 35 seconds and try again")
        time.sleep(35)
        print("try again")
        bot.send_document(document=open(filename, 'rb'), **kwargs)

def send_notification(
        text='test', files=None, text_for_files=None, chat_id=chat_id, token=token
):
    try:
        bot = telegram.Bot(token=token)
        if text:
            if len(text) > 4096:
                f_name = 'long_message_{}.txt'.format(time.time())
                with open(f_name, "w") as f:
                    f.write(text)
                send_document(
                    bot=bot, filename=f_name, chat_id=chat_id,
                    caption="too long message -> send as file")
                os.remove(f_name)
            else:
                send_message(bot=bot, chat_id=chat_id, text=text)
        if files:
            for f in files:
                send_document(bot=bot, filename=f, chat_id=chat_id,
                              caption=text_for_files)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    send_notification(files=['../test.txt'], text_for_files='test-file')
    # send_notification("="*5000)