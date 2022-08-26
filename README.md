# Programming-vacancies-compare
This script analyses salaries for different programming jobs and organizes data in two tables with average salaries for [15 most popular programming langugages](https://habr.com/ru/post/310262/). The script uses two sources with job vacancies: [HeahHunter](https://hh.ru/) and [SuperJob](https://www.superjob.ru/).

## How to install

HeahHunter doesn't require any authorization, but in order to get data from SuperJob you need to register your app [here](https://api.superjob.ru/register). For more information please read [SuperJob API Documentation](https://api.superjob.ru/).

When you complete the registration you will be given a secret key. Create a file with the name .env in the same directory with the script. Paste your login and password in the file:

```
SUPERJOB_SECRET_KEY = 'your secret key'
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:

```
pip install -r requirements.txt
```

Launch

```
python main.py
```

## Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).