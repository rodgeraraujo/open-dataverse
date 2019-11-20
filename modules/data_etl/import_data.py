import argparse
import csv
import json
import traceback
import sys, os
from collections import OrderedDict
from pymongo import MongoClient
import pandas as pd


def csv2Mongo(csvfile, database_name,collection_name, host, port):
    response_dict = OrderedDict()
    mc = MongoClient(f'mongodb://{host}:{port}/')
    db = mc[database_name]
    collection = db[collection_name].delete_many({})
    print(collection)
    try:
        mc = MongoClient(f'mongodb://{host}:{port}/')
        db = mc[database_name]
        collection = db[collection_name]
        # open the csv file.
        csvhandle = csv.reader(open(csvfile, 'r'), delimiter=',')

        rowindex = 0
        mongoindex = 0
        error_list = []

        for row in csvhandle:

            if rowindex == 0:
                column_headers = row
                cleaned_headers = []
                for c in column_headers:
                    c = c.replace(".", "")
                    c = c.replace("(", "")
                    c = c.replace(")", "")
                    c = c.replace("$", "-")
                    c = c.replace(" ", "_")
                    cleaned_headers.append(c)
            else:

                record = OrderedDict(zip(cleaned_headers, row))
                try:
                    print(record)
                    myobjectid = collection.insert(record)
                    mongoindex += 1

                except:
                    error_message = "Error on row " + \
                        str(rowindex) + ". " + str(sys.exc_info())
                    error_list.append(error_message)

            rowindex += 1

        if error_list:
            response_dict['num_rows_imported'] = rowindex
            response_dict['num_rows_errors'] = len(error_list)
            response_dict['errors'] = error_list
            response_dict['code'] = 400
            response_dict['message'] = "Completed with errors"
        else:

            response_dict['num_rows_imported'] = mongoindex
            response_dict['num_csv_rows'] = rowindex
            response_dict['code'] = 200
            response_dict['message'] = "Completed."
        
    except:
        response_dict['code'] = 500
        response_dict['errors'] = [traceback.print_exc()]
    
    return response_dict

def filterCsv(file_name, currentDirectory):
    csv = currentDirectory + "/files/"+file_name+".csv"

    data = pd.read_csv(csv, index_col = 0)
    data.columns = data.columns.str.replace("[.]", "_")

    data.head()

    if file_name == "aluno":
        data.query('curso_nome == "201 - Tecnologia em Análise e Desenvolvimento de Sistemas - Cajazeiras (CAMPUS CAJAZEIRAS)"', inplace = True)
        data.query('situacao != "Cancelado"', inplace = True)
        new_name = "students"
    else:
        data.query('cargo_emprego == "PROFESSOR ENS BASICO TECN TECNOLOGICO"', inplace = True)
        data.query('disciplina_ingresso != "UNINFO-CZ"', inplace = True)
        new_name = "teachers"

    new_file = currentDirectory+"/files/"+new_name+".csv"
    data.to_csv(new_file)

    return new_file

async def run_import(file_name):
    # current directory
    currentDirectory = os.getcwd()
    # csv_file = '/home/rodger/TCC/open-dataverse/modules/data_etl/files/'+file_name+'.csv'
    database = 'dataverse'
    collection = file_name
    host = 'mongodb'
    port = 27017

    csv_file = filterCsv(file_name, currentDirectory)

    result = csv2Mongo(csv_file, database, collection, host, port)
    # output the JSON transaction summary
    print(json.dumps(result, indent=4))