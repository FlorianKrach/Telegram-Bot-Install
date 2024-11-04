# Telegram-Bot

This is a package for sending notifications to a chat 
using a telegram bot.

It has a certain chat_id and a bot token saved for easy use.

To get chat_id of a chat where a bot with token ```<token>``` was added:
- in this chat send the message "/test"
- in a browser open: ```https://api.telegram.org/bot<token>/getUpdates```


## Installation

Download or clone this repo, then run:
```shell
cd Telegram-Bot-Install
python setup.py install
```
this will install the package and all requirements. It will also ask you for the
token of your telegram bot to install it as default (=> you don't need to specify it
every time you send a message).


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

