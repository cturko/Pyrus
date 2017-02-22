#!/usr/bin/env python
# -*- coding: utf-8 -*-
import platform

profile = ['architecture',
           'linux_distribution',
           'mac_ver',
           'machine',
           'node',
           'platform',
           'processor',
           'python_build',
           'python_compiler',
           'python_version',
           'release',
           'system',
           'uname',
           'version']

def main():
    print("")
    for key in profile:
        if hasattr(platform, key):
            print(key + ": " + str(getattr(platform, key)()))
    print("")

if __name__ == '__main__':
    main()
