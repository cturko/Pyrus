#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request

try:
    urllib.request.urlopen('https://google.ca')
    print('Connected.')

except urllib.error.URLError:
    print('No connection.')
