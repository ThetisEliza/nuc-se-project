from flask import Flask, jsonify, Response, request
import sys
from model.data import Group
import json


class System:
    def __init__(self) -> None:
        self.groups = []

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


if __name__ == '__main__':
    app.run(port=8080, host='172.24.43.114', debug=True)