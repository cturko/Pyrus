import urllib.request

def check_connection():
    try:
        urllib.request.urlopen('https://duckduckgo.com')
        print("Success: Connected")

    except urllib.error.URLError:
        print("Error: No Connection")

check_connection()
