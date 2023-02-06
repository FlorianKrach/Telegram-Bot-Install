"""
author: Florian Krach
"""
import os.path

import setuptools
import inspect
import atexit
from setuptools.command.install import install


def _post_install():
    print('POST INSTALL')
    import telegram_notifications
    token = input("Please enter the token of your Telegram Bot:")
    path = os.path.abspath(inspect.getfile(telegram_notifications))
    filename = os.path.join(path, "send_bot_message.py")
    with open(filename, "r") as f:
        lines = f.readlines()
    newlines = []
    for line in lines:
        if line.strip().startswith("token"):
            line = "token = '{}'".format(token)
        newlines.append(line)
    with open(filename, "w") as f:
        f.writelines(newlines)



class new_install(install):
    def __init__(self, *args, **kwargs):
        super(new_install, self).__init__(*args, **kwargs)
        atexit.register(_post_install)



with open("README.md", "r") as fh:
    long_description = fh.read()





setuptools.setup(
    name="telegram-bot",
    version="0.0.1",
    author="Florian Krach",
    author_email="florian.krach@me.com",
    description="easy package for sending notifications with a telegram bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["python-telegram-bot==12.8"],
    cmdclass={'install': new_install},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)


