import requests


def get_content_type(url):
    r = requests.get(url)
    return r.headers['content-type']

# print(get_content_type('http://google.com'))
# print(get_content_type('http://github.com'))