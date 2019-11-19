import argparse
import csv
import json
import traceback
import sys, os
from collections import OrderedDict
from pymongo import MongoClient


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

def run(file_name):
    # current directory
    currentDirectory = os.getcwd()
    csv_file = '/home/rodger/TCC/open-dataverse/modules/data_etl/files/'+file_name+'.csv'
    database = 'dataverse'
    collection = file_name
    host = 'localhost'
    port = 27017

    result = csv2Mongo(csv_file, database, collection, host, port)
    # output the JSON transaction summary
    print(json.dumps(result, indent=4))