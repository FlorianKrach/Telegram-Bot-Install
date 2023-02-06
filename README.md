# Telegram-Bot

This is a package for sending notifications to a chat 
using a telegram bot.

It has a certain chat_id and a bot token saved for easy use.

To get chat_id of a chat where a bot with token ```<token>``` was added:
- in this chat send the message "/test"
- in a browser open: ```https://api.telegram.org/bot<token>/getUpdates```


## Installation

```shell
cd Telegram-Bot
pip install dist/telegram_bot-0.0.1-py3-none-any.whl --upgrade
```


install from github:
```shell
pip install git+https://github.com/FlorianKrach/Telegram-Bot
```



requirements (automatically installed):
```
pip install python-telegram-bot==12.8 --upgrade
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

## Update package
- update code
- run ```python setup.py bdist_wheel``` to update the package
- git push
- on all devices run 
```pip install dist/telegram_bot-0.0.1-py3-none-any.whl --upgrade``` to 
update the package (after pulling)


