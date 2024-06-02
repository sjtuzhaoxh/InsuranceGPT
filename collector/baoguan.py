import requests
from bs4 import BeautifulSoup

base_url = 'http://wiki.baoxianguancha.com/'

def save(html, name):
    path = 'D:\\data\\baoguan\\'
    name = name + '.html'
    with open(path + name, 'w', encoding='utf-8') as f:
        f.write(html)

def get_html(url):
    print("fetching:" + url)
    response = requests.get(url)
    return response.text


def crawler(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    a_tags = soup.find_all('a')
    for tag in a_tags:
        if tag.get('href') == '/' or tag.get('href') == '':
            continue
        sub_url = tag.get('href')
        if sub_url is None:
            continue
        if sub_url.startswith('./'):
            sub_url = sub_url.replace("./", "/")
        if sub_url.startswith('doc-view'):
            print(sub_url, tag.get_text())
            save(html, tag.get_text())
            crawler(base_url + sub_url)


if __name__ == '__main__':
    crawler(base_url)