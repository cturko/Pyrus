#!/usr/bin/env/python
# -*- coding: utf-8 -*-
import urllib.request

def tiny_url(web_address):
    target = 'http://tinyurl.com/api-create.php?url=' + web_address
    response = urllib.request.urlopen(target)
    return response.read()

def main():
    web_address = input("Enter URL: ")
    print(tiny_url(web_address))

    
if __name__ == '__main__':
    main()
