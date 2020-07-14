from bs4 import NavigableString, BeautifulSoup
from collections import deque
from colorama import Fore, Style
import os
import requests
import sys

user_url = ''
files = deque()
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0'}


def short_url(url):
    if url.count('.') > 1:
        result = url[:-url[::-1].find('.') - 1]
    else:
        result = url[:url.find('.')]
    return result


if not os.path.exists(sys.argv[1]):
    os.mkdir(sys.argv[1])

while user_url != 'exit':
    user_url = input()
    if user_url == 'back' and len(files) > 0:
        with open(f'{sys.argv[1]}/{files[len(files) - 2]}.txt', 'r') as f:
            print(f.read())
        files.pop()
    elif '.' not in user_url and user_url not in files:
        print('Error: Incorrect URL')
    elif user_url in files:
        with open(f'{sys.argv[1]}/{user_url}.txt', 'r') as f:
            print(f.read())
    else:
        with open(f'{sys.argv[1]}/{short_url(user_url)}.txt', 'w', encoding="utf-8") as f:
            files.append(short_url(user_url))
            if not user_url.startswith('https://'):
                user_url = 'https://' + user_url
            r = requests.get(user_url, headers=headers)
            soup = BeautifulSoup(r.content, 'html.parser')
            text = []
            tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
            for child in soup.descendants:
                if (isinstance(child, NavigableString) and child.parent.name in tags) \
                        and len(str(child.string).strip(' \n')) > 0:
                    if child.parent.name == 'a':
                        print(Fore.BLUE + str(child.string).strip(' \n'))
                        print(Style.RESET_ALL, end='')
                    else:
                        print(str(child.string).strip(' \n'))
                    text.append(str(child.string).strip(' \n'))
            f.write('\n'.join(text))
