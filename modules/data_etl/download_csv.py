import os

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

async def run_download(value):
    if value == "aluno":
        url = "https://dados.ifpb.edu.br/dataset/d02eb6b8-5745-4436-ae22-ef1c182897d9/resource/29c2b593-ed14-4b73-b30c-d6135f072cf7/download/alunos.csv"
    else:
        url = "https://dados.ifpb.edu.br/dataset/26d67876-0cb2-41a4-83ed-7bde06eb736c/resource/c2406ee2-fa8f-4500-a44f-0ce8fb6bb1b7/download/servidores.csv"
    csvDownload(url, value)