import urllib.request

try:
    urllib.request.urlopen('https://duckduckgo.com')
    print("Success: Connected.")

except urllib.error.URLError:
    print("Error: No Connection.")
