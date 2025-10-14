# Telegram-Bot

This is a package for sending notifications to a chat 
using a telegram bot.

It has a certain chat_id and a bot token saved for easy use.

First you need a Telegram-Bot, i.e., its `token`. If you do not yet have one, you can get a token following these [instructions](https://core.telegram.org/bots/features#creating-a-new-bot).

To get the chat_id of a chat where a bot with token ```<token>``` was added:
- in this chat send the message "/test"
- in a browser open: ```https://api.telegram.org/bot<token>/getUpdates```


## Release note:
- if using python<3.9 use the release v1.0.1 which works with python-telegram-bot==12.8
- if using python>=3.9 use the release v2.0.0 which works with python-telegram-bot==22.5


## Installation

### Manual installation
Download or clone this repo, then run

```shell
cd Telegram-Bot-Install
pip install dist/telegram_bot-<version>-py3-none-any.whl --upgrade

# latest version
pip install dist/telegram_bot-2.0.0-py3-none-any.whl --upgrade
```
this will install the package and all requirements. 

### Installation from GitHub
One can directly install the package from GitHub by running:

```shell
# latest version
pip install git+https://github.com/FlorianKrach/Telegram-Bot-Install

# version v2.0.0
pip install git+https://github.com/FlorianKrach/Telegram-Bot-Install@v2.0.0

# version v1.0.1
pip install git+https://github.com/FlorianKrach/Telegram-Bot-Install@v1.0.1
```

### Token info

For using the telegram-bot without providing the token each time, the token can for example be placed in the installed package file `send_bot_message.py`.


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

