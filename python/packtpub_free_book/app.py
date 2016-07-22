#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def main():
    url = 'https://www.packtpub.com/packt/offers/free-learning'

    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
    except:
        raise Exception('problem with connection or parsing')

    # try block for basic book informations
    try:
        # title 
        title = soup.find("div", class_="dotd-title").getText().strip()

        # picture
        pic = soup.find("div", class_="dotd-main-book-image float-left").find("img")['src'].strip()
        pic = pic.replace(' ', '%20')
        if pic.startswith('//'):
            pic = pic.replace('//','http://')
    except AttributeError:
        raise Exception('problem with parsing')
    else:
        print('Title:', title)
        print('Image:', pic)

    # try block for additional book informations
    try:
        info = []
        for i in soup.find("div", class_="dotd-main-book-summary float-left").find_all("div"):
            ret = i.getText().strip()
            if 'Time is running out' not in ret \
                and ret is not '' \
                and title not in ret:
                info.append(ret)
    except AttributeError:
        pass
    else:
        print('Infos:...')
        for x in info: print(x)


if __name__ == '__main__':
    main()