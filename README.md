# Telegram-Bot

Release note:
- if using python<3.9 use the release v1.0.1 which works with python-telegram-bot==12.8
- if using python>=3.9 use the release v2.0.0 which works with python-telegram-bot==22.5

This is a package for sending notifications to a chat 
using a telegram bot.

It has a certain chat_id and a bot token saved for easy use.

First you need a Telegram-Bot, i.e., its `token`. If you do not yet have one, you can get a token following these [instructions](https://core.telegram.org/bots/features#creating-a-new-bot).

To get the chat_id of a chat where a bot with token ```<token>``` was added:
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
SBM.send_notification(text='', files=['README.md',], text_for_files='test-file')
```

send message and files to certain chat_id with certain token (bot identifier)
```
SBM.send_notification(text='', files=['README.md',], chat_id="...", token="...")
```

