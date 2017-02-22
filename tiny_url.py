#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import urllib.request
import sys

def tiny_url(web_address):
    target = 'http://tinyurl.com/api-create.php?url=' + web_address
    response = urllib.request.urlopen(target)
    return response.read()

def main():
    while True:
        web_address = input("Enter URL: ")
        if web_address == 'quit':
            sys.exit()
        else:
            print(tiny_url(web_address))


if __name__ == '__main__':
    main()

