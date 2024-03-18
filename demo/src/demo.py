from flask import Flask, jsonify, Response, request, abort
import sys
from model.data import Group
import json
from typing import List
from dao.database_model import DatabaseBzController

class System:
    def __init__(self) -> None:
        self.dbc = None

    def load_sys(self) -> 'System':
        self.dbc = DatabaseBzController()
        return self

import os
os.environ['LANG'] = 'en_US.UTF-8'
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.json.ensure_ascii = False
system = System().load_sys()


def allowCrossSite(response: Response) -> Response:
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Method'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    return response
    
##########################
# Group Full status api
##########################
@app.route('/api/groups/all')
def get_all_groups():
    data = {
        "groups": system.dbc.getAllGroups(None),
    }
    return allowCrossSite(jsonify(data))

@app.route('/api/groups/page')
def get_page_groups():
    print(request.args)
    # request_data = request.json
    page_num = request.args.get('pageNum', '0')
    page_size = request.args.get('pageSize', '1')
    sort_with = request.args.get('sortBy[0][key]')
    sort_order = request.args.get('sortBy[0][order]', 'desc')   
    page_num = int(page_num)
    page_size = int(page_size)
    groups, total = system.dbc.getPageGroups(page_num, page_size, sort_with, sort_order)
    data = {
        "groups": groups,
        "total": total
    }
    res = jsonify(data)
    return allowCrossSite(res)


##########################
# User status api
##########################

@app.route('/api/admin/login')
def login():
    print(request)
    user = request.args.get("username")
    pswd = request.args.get("password", 0)
    mock_list = {
        'qwe': 'qwe',
        'admin': 12345,
        'admin1': 123451,
        'admin2': 123452
    }
    login_status = 0
    if user in mock_list:
        if mock_list[user] == pswd:
            login_status = 0
            msg = 'OK'
        else:
            login_status = 1
            msg = 'Password error'
    else:
        login_status = 2
        msg = 'User not found'
        
    data = {
        "user": user,
        "status": login_status,
        "msg": msg
    }
    if login_status != 0:
        abort(allowCrossSite(jsonify(data)))
    return allowCrossSite(jsonify(data))

from datetime import datetime

##########################
# Admin Group CRUD API
##########################

def find_group(_id) -> Group:
    res = list(filter(lambda x: x._id == _id, system.dbc.getAllGroups()))
    if len(res) == 0:
        return None
    else:
        return res[0]
    
@app.route('/api/group/details')
def get_group_details():
    print(request.args)
    _id = request.args.get('groupid', 0)
    group = find_group(_id)
    if group is None:
        abort(allowCrossSite(Response("group not found")))
    return allowCrossSite(jsonify(group))

@app.route('/api/group/modifyscore')
def modify_group_score():
    print(request.args)
    _id = request.args.get('groupId')
    score = request.args.get('score', 0)
    print(_id, score)
    res = system.dbc.updateGroupScore(_id, float(score))
    data = {
        "msg": "ok",
        "status": res
    }
    return allowCrossSite(jsonify(data))

def add_group():
    res = jsonify(system.groups)
    return allowCrossSite(res)

def remove_group():
    res = jsonify(system.groups)
    return allowCrossSite(res)

def add_group_member():
    res = jsonify(system.groups)
    return allowCrossSite(res)

def remove_group_member():
    res = jsonify(system.groups)
    return allowCrossSite(res)

def get_idle_members():
    res = jsonify(system.groups)
    return allowCrossSite(res)


if __name__ == '__main__':
    app.run(port=8080, host='172.24.43.114', debug=True)