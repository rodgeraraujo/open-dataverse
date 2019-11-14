import os
import sys
import requests

# import logger
# from app import app
from download_data import download_data
# from import_data import import_data

if __name__ == '__main__':

    url = "https://dados.ifpb.edu.br/dataset/d02eb6b8-5745-4436-ae22-ef1c182897d9/resource/29c2b593-ed14-4b73-b30c-d6135f072cf7/download/alunos.csv"
    type_data = "aluno"

    download_data.data.downloadData(url, type_data)