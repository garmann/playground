#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


def soup_object(url):
    """generates and returns soup object for given url

    Args:
        url - string: url of a website, here its packtpub
    Returns:
        soup - object: the soup object for later parsing
    Raises:
        Exception: if there is a problem with connection or parsing
    """
    try:
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
    except:
        raise Exception('problem with connection or parsing')
    else:
        return soup


def parse_title(soup):
    """parses title of the book

    Args:
        soup - object: the soup object to parse
    Returns:
        title - string
    Raises:
        Exception: if soup cannot find the given div/class
    """
    try:
        title = soup.find("div", class_="dotd-title").getText().strip()
    except AttributeError:
        raise Exception('problem with parsing')
    else:
        return title


def parse_picture_url(soup):
    """parses url of book image and some minor changes to the string

    Args:
        soup - object: the soup object to parse
    Returns:
        pic - string: the url of the book image
    Raises:
        Exception: if soup cannot find the given div/class
    """
    try:
        pic = soup.find("div", class_="dotd-main-book-image float-left").find("img")['src'].strip()
        pic = pic.replace(' ', '%20')
        if pic.startswith('//'):
            pic = pic.replace('//','http://')
    except AttributeError:
        raise Exception('problem with parsing')
    else:
        return pic


def parse_description(soup, title):
    """parses description of the book

    Args:
        soup - object: the soup object to parse
        title - string: book title
    Returns:
        info - list: the description of the book
    Raises:
        raises nothing: if no description is found, just continue
    """
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
        return info


def return_url(url):
    """ returns url string
    this function will be used by a chatbot
    """
    return url


def main():
    """handles site parsing of the packtpub site for free ebooks and prints all informations
    """
    url = 'https://www.packtpub.com/packt/offers/free-learning'
    soup = soup_object(url)

    print('title:', parse_title(soup))
    print('imageurl:', parse_picture_url(soup))
    print('description:...')
    for line in parse_description(soup, parse_title(soup)): print(line)
    print('url:', return_url(url))


if __name__ == '__main__':
    main()
    