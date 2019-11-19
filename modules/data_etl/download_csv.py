import os
# from .database import *

import requests
import os

def csvDownload(url, type):
    try:
        path = os.getcwd()
        directory = "files"
        if not os.path.exists(directory):
            os.makedirs(directory)

        print("Request file")
        r = requests.get(url)
        print("Download file")
        with open(path + '/files/' + type + ".csv", 'wb') as f:
            f.write(r.content)
        print("File downloaded")
        print("Completed...!")
    except requests.exceptions.RequestException as e:
        print("Error when try download file content")
        print(e)