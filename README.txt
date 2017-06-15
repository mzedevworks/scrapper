scrapper
========

Getting Started
---------------
- This project will scrape a given wikipedia url to get the table of contents

- Below are the steps to set it up

- First clone the project anywhere you wish on your local machine

- Change directory into your newly created project.

    cd scrapper

- Create a Python virtual environment.

    python3 -m venv env

- Upgrade packaging tools.

    env/bin/pip install --upgrade pip setuptools

- Install the project in editable mode with its testing requirements.

    env/bin/pip install -e ".[testing]"

- Run your project's tests.

    env/bin/pytest

- Run your project.

    env/bin/pserve development.ini
