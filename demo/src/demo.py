from flask import Flask, jsonify, Response, request, abort
import sys
from model.data import Group
import json
from typing import List


class System:
    def __init__(self) -> None:
        self.groups: List[Group] = []

    def load_sys(self) -> 'System':
        with open('/home/phoenix/projects/nuc-se-project/demo/tmp/groups.jsonl') as f:
            for line in f:
                self.groups.append(Group.parse(line.strip()))
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
    res = jsonify(system.groups)
    return allowCrossSite(res)

@app.route('/api/groups/page')
def get_page_groups():
    print(request.args)
    # request_data = request.json
    page_num = request.args.get('pageNum', 0)
    page_size = request.args.get('pageSize', 0)
    page_num = int(page_num) - 1
    page_size = int(page_size)
    
    data = {
        "groups": system.groups[page_size*page_num:page_size*(page_num+1)],
        "total": len(system.groups)
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
        else:
            login_status = 1
            abort(allowCrossSite(Response("Password error")))
    else:
        login_status = 2
        abort(allowCrossSite(Response("User not found")))
    data = {
        "user": user,
        "status": login_status
    }
    return allowCrossSite(jsonify(data))



##########################
# Admin Group CRUD API
##########################

def find_group(_id) -> Group | None:
    res = list(filter(lambda x: x._id == _id, system.groups()))
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
    _id = request.args.get('groupid', 0)
    score = request.args.get('score', 0)
    group = find_group(_id)
    if group is None:
        abort(allowCrossSite(Response("group not found")))
    group.score = score    
    return allowCrossSite(jsonify(group))

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