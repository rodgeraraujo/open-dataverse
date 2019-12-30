''' controller and routes for teachers '''
import os
from flask import request, jsonify
from app import app, mongo
import logger
import json
from bson import json_util

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/teachers', methods=['GET'])
def teachers():
    ''' route read teachers data '''
    if request.method == 'GET':
        data = mongo.db.servidores.find()
        
        teachers_list = []
        for teacher in data:
            teachers_list.append(teacher)
    
        return json.dumps(teachers_list, default=json_util.default), 200