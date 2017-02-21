#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""
Open Weather Map API. Currently runs as a stand-alone script.
Arguments:
            --help      Displays this message.
            --config    Enter config file information.
Returns:
            Detailed weather information from OpenWeatherMap.org

Required Configuration:
            OWM API key: http://openweathermap.org/appid
            OWM city ID: http://bulk.openweathermap.org/sample/city.list.json.gz
            Preferred Unit: metric, imperial, or kelvin

Usage:      Run python weather.py --config for the first time to setup
            configuration information.
            After config file is setup, run python weather.py for weather info.

Source: https://github.com/mzdhr/weather
"""
import configparser
import datetime
import json
import sys
import urllib.request

def build_url(city_id, user_api, unit):
    api = 'http://api.openweathermap.org/data/2.5/weather?id='
    api_url = api + city_id + '&mode=json&units=' + unit + '&APPID=' + user_api
    return api_url

def retrieve_data(api_url):
    with urllib.request.urlopen(api_url) as url:
        output = url.read().decode('utf-8')
        raw_api_dict = json.loads(output)
    return raw_api_dict

def organize_data(raw_data):
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = dict(
        city=raw_data.get('name'),
        country=sys.get('country'),
        temp=main.get('temp'),
        temp_max=main.get('temp_max'),
        temp_min=main.get('temp_min'),
        humidity=main.get('humidity'),
        pressure=main.get('pressure'),
        sky=raw_data['weather'][0]['main'],
        sunrise=convert_time(sys.get('sunrise')),
        sunset=convert_time(sys.get('sunset')),
        wind=raw_data.get('wind').get('speed'),
        wind_deg=raw_data.get('deg'),
        dt=convert_time(raw_data.get('dt')),
        cloudiness=raw_data.get('clouds').get('all')
    )
    return data

def convert_time(time):
    converted_time = datetime.datetime.fromtimestamp(
        int(time)).strftime('%I:%M %p')
    return converted_time

def send_to_display(city_id, user_api, prefer_unit):
    setting = build_url(city_id=city_id,
                          user_api=user_api,
                          unit=prefer_unit)
    raw_data = retrieve_data(setting)
    data = organize_data(raw_data)
    display(data)

def display(data):
    m_symbol = '\xb0' + 'C'
    print("Current weather in {}, {}:".format(data['city'], data['country']))
    print(data['temp'], m_symbol, data['sky'])
    print("Max: {}, Min: {}".format(data['temp_max'], data['temp_min']))
    print("Wind Speed: {}, Degree: {}".format(data['wind'], data['wind_deg']))
    print("Humidity: {}".format(data['humidity']))
    print("Cloud: {}".format(data['cloudiness']))
    print("Pressure: {}".format(data['pressure']))
    print("Sunrise: {}".format(data['sunrise']))
    print("Last updated: {}".format(data['dt']))

def save_config():
        city_id = input("OWM City ID: ")
        user_api = input("OWM API: ")
        prefer_unit = input("Preferred unit [metric, imperial, kelvin]: ")

        config = configparser.ConfigParser()
        config['DEFAULT'] = {'city_id': city_id,
                             'user_api': user_api,
                             'prefer_unit': prefer_unit}

        with open('weather_config.ini', 'w') as configfile:
            config.write(configfile)

def load_config():
    try:
        config = configparser.ConfigParser()
        config.read('weather_config.ini')
        city_id = config.get('DEFAULT', 'city_id')
        user_api = config.get('DEFAULT', 'user_api')
        prefer_unit = config.get('DEFAULT', 'prefer_unit')

        send_to_display(city_id, user_api, prefer_unit)

    except AttributeError as missing_data:
        print("Missing city_id or prefer_unit in the config file", missing_data)

    except urllib.error.HTTPError as apiError:
        print("Missing or unauthorized API in the config file.", apiError)

    except IOError as e:
        print("Error, no internet connection", e)

    except configparser.NoOptionError as fi:
        print("Config file not found, reload config file using '--config'", fi)

def argv():
    args = sys.argv
    args.pop(0)
    if len(args) != 0:
        if args[0] == '--config':
            save_config()
        elif args[0] == '--help':
            print(__doc__)
            sys.exit()
        else:
            print("Unknown command, use --help for more information.")
            sys.exit()

def main():
    argv()
    load_config()


if __name__ == '__main__':
    main()
