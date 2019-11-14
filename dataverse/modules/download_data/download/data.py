import requests
import os

def downloadData(url, type):
    try:
        path = os.getcwd()
        print("1 - Request file")
        r = requests.get(url)
        print("2 - Download file")
        with open(path + '/files/' + type + ".csv", 'wb') as f:
            f.write(r.content)
        print("3 - File downloaded...")
        print("4 - Finish")
    except requests.exceptions.RequestException as e:
        print(e)