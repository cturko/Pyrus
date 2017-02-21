#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import sys


def roll(side_value):
    return random.randint(1, side_value)

def main():
    while True:
        sides = input("[d4, d6, d8, d10, d12, d20]: ")
        if sides == 'quit':
            sys.exit()
        else:
            side_value = int(sides.replace("d", ""))
            print(roll(side_value))


if __name__ == '__main__':
    main()
