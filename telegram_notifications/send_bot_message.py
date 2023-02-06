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
                bot.send_document(chat_id=chat_id, document=open(f_name, 'rb'),
                                  caption="too long message -> send as file")
                os.remove(f_name)
            else:
                bot.send_message(chat_id=chat_id, text=text)
        if files:
            for f in files:
                bot.send_document(chat_id=chat_id, document=open(f, 'rb'),
                                  caption=text_for_files)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    send_notification(files=['../test.txt'], text_for_files='test-file')
    # send_notification("="*5000)