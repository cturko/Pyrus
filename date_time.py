#!/usr/bin/env python
# -*_ coding: utf-8 -*-
import datetime
import sys


def main():

    now = datetime.datetime.now()

    while True:
        user_request = input("\nCurrent [time, day, date]: ")

        if user_request == "quit":
            sys.exit()

        if user_request == "time":
            second = str(now.second)
            time_request = (str(now.hour)
                            + ":"
                            + str(now.minute)
                            + ":"
                            + str(now.second))
            print("\nIt is: " + time_request)

        if user_request == "day":
            day_request = str(now.strftime("%A"))
            print("\nIt is " + day_request)

        if user_request == "date":
            date_request = (str(now.year)
                            + "-"
                            + str(now.month)
                            + "-"
                            + str(now.day))
            print("\nIt is: " + date_request)


if __name__ == '__main__':
    main()
