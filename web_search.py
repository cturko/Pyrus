#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import urllib.request
import sys

def web_search(search_input):

    search_input = search_input
    ddg_url = 'http://api.duckduckgo.com/?q='
    ddg_format = '&format=json&pretty=1'

    ddg_input = search_input.replace(" ", "%20")
    ddg_search = urllib.request.urlopen(ddg_url + ddg_input + ddg_format)

    ddg_read = ddg_search.read()
    ddg_decode = json.loads(ddg_read.decode('utf-8'))
    ddg_read = ddg_decode
    json_string = json.dumps(ddg_read, sort_keys=True, indent=2)

    return json_string

def main():

    while True:
        search_input = input("Enter your query: ")
        if search_input == "quit":
            sys.exit()
        else:
            web_search(search_input)
            print(json_string)

if __name__ == '__main__':
    print("DuckDuckGo API Python Script")
    main()
