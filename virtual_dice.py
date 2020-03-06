import random
import sys


def roll(side_value):
    return random.randint(1, side_value)

def main():
    while True:
        sides = input("[d4, d6, d8, d10, d12, d20, or quit]: ")
        if sides == 'quit':
            sys.exit()
        else:
            side_value = int(sides.replace('d', ''))
            print(roll(side_value))

main()
