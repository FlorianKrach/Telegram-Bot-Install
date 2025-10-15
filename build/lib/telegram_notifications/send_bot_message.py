"""
author: Florian Krach
"""

# ==============================================================================
# IMPORTS
import logging

# the following supresses the extensive logging of the telegram package to the IO
logging.getLogger("telegram").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

import telegram
import time
import os
import asyncio

# ==============================================================================
# GLOBAL VARIABLES

# token for the bot:
token = None

# chat id for: Cloud-Computing-Notifiications
chat_id = None


# ==============================================================================
async def send_message(bot, n_try=0, max_tries=10, wait_time=35, **kwargs):
    try:
        await bot.send_message(**kwargs)
    except Exception as e:
        print("TELEGRAM BOT: Error while sending message:")
        print(e)
        if n_try < max_tries:
            print(f"wait for {wait_time} seconds and try again")
            time.sleep(wait_time)
            print(f"try again (n_try={n_try+2}/{max_tries})")
            await send_message(
                bot, n_try=n_try+1, max_tries=max_tries,
                wait_time=wait_time, **kwargs)
        else:
            print(f"TELEGRAM BOT: max tries ({max_tries}) reached for sending message "
                  f"-> abort sending message")

async def send_document(
        bot, n_try=0, max_tries=10, wait_time=35, filename=None, **kwargs
):
    try:
        await bot.send_document(document=open(filename, 'rb'), **kwargs)
    except Exception as e:
        print("TELEGRAM BOT: Error while sending document:")
        print(e)
        if n_try < max_tries:
            print(f"wait for {wait_time} seconds and try again")
            time.sleep(wait_time)
            print(f"try again (n_try={n_try+2}/{max_tries})")
            await send_document(
                bot, n_try=n_try+1, max_tries=max_tries, wait_time=wait_time,
                filename=filename, **kwargs)
        else:
            print(f"TELEGRAM BOT: max tries ({max_tries}) reached for sending document "
                  f"-> abort sending document")

async def _send_notification(
        text='test', files=None, text_for_files=None, chat_id=chat_id,
        token=token, max_tries=10, wait_time=35,
):
    try:
        bot = telegram.Bot(token=token)
        async with bot:
            if text:
                if len(text) > 4096:
                    f_name = 'long_message_{}.txt'.format(time.time())
                    with open(f_name, "w") as f:
                        f.write(text)
                    await send_document(
                        bot=bot, filename=f_name, chat_id=chat_id,
                        n_try=0, max_tries=max_tries, wait_time=wait_time,
                        caption="too long message -> send as file")
                    os.remove(f_name)
                else:
                    await send_message(
                        bot=bot, chat_id=chat_id, text=text,
                        n_try=0, max_tries=max_tries, wait_time=wait_time)
            if files:
                for f in files:
                    await send_document(
                        bot=bot, filename=f, chat_id=chat_id, caption=text_for_files,
                        n_try=0, max_tries=max_tries, wait_time=wait_time)
    except Exception as e:
        print(e)


def send_notification(
        text='test', files=None, text_for_files=None, chat_id=chat_id,
        token=token, max_tries=10, wait_time=35,
):
    asyncio.run(_send_notification(
        text=text, files=files, text_for_files=text_for_files, chat_id=chat_id, token=token))



if __name__ == '__main__':
    send_notification(files=['../test.txt'], text_for_files='test-file')
    # send_notification("="*5000)
