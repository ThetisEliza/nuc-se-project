from flask import Flask
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


app = Flask(__name__)

system = System().load_sys()
    
    
@app.route('/')
def index():
    return 'welcome to my webpage!'

@app.route('/groups/all')
def get_all_groups():
    return json.dumps(list(map(lambda x: x.__dict__, system.groups)), ensure_ascii=False)

@app.route('/groups/page/<int:pageId>')
def get_page_groups(pageId):
    return json.dumps(list(map(lambda x: x.__dict__, system.groups))[5*pageId:5*(pageId+1)], ensure_ascii=False)


if __name__ == '__main__':
    
    app.run(port=8080, host='172.24.43.114', debug=True)