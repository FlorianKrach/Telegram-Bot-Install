# Telegram-Bot

This is a package for sending notifications to a chat 
using a telegram bot.

It has a certain chat_id and a bot token saved for easy use.

To get chat_id of a chat where a bot with token ```<token>``` was added:
- in this chat send the message "/test"
- in a browser open: ```https://api.telegram.org/bot<token>/getUpdates```


## Installation

Download or clone this repo, then open the file `telegram_notifications/send_bot_message.py`
and replace the `token = None` by `token = "<your-bot-token>"` (follow this [tutorial](https://core.telegram.org/bots/tutorial) 
to get the token). If you want you can also add a default chat_id. Then

```shell
cd Telegram-Bot-Install
python setup.py install
```


## Usage
```
from telegram_notifications import send_bot_message as SBM
```

send message and files with default token to default chat_id
```
SBM.send_notification(text='', files=['test.txt',], text_for_files='test-file')
```

send message and files to certain chat_id with certain token (bot identifier)
```
SBM.send_notification(text='', files=['test.txt',], chat_id="...", token="...")
```

