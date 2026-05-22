"""author: Florian Krach"""

import setuptools

with open("README.md", "r") as fh:  # noqa: PTH123
    long_description = fh.read()


setuptools.setup(
    name="telegram-bot",
    version="2.2.0",
    author="Florian Krach",
    author_email="florian.krach@me.com",
    description="simple package for sending notifications with a telegram bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    install_requires=["python-telegram-bot==22.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
