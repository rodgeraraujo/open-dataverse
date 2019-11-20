''' controller and routes for students '''
import os
from flask import request, jsonify
from app import app, mongo
import logger
import json
from bson import json_util

ROOT_PATH = os.environ.get('ROOT_PATH')
LOG = logger.get_root_logger(
    __name__, filename=os.path.join(ROOT_PATH, 'output.log'))


@app.route('/students', methods=['GET', 'POST', 'DELETE', 'PATCH'])
def students():
    ''' route read students data '''
    if request.method == 'GET':
        data = mongo.db.aluno.find()
        
        students_list = []
        for student in data:
            students_list.append(json.dumps(student, default=json_util.default))
    
        return jsonify(students_list), 200

    data = request.get_json()
    if request.method == 'POST':
        if data.get('name', None) is not None and data.get('email', None) is not None:
            mongo.db.students.insert_one(data)
            return jsonify({'ok': True, 'message': 'Student created successfully!'}), 200
        else:
            return jsonify({'ok': False, 'message': 'Bad request parameters!'}), 400