import json
from typing import List
from flask import Flask, jsonify, Response, request, abort
import logging

from app import create_app
from app.middleware import register_middleware
from app.model.data import Group, Member
from app.dao.database_model import DatabaseBzController
from app.utils.pack_response import pack_response, pack_error

nuc_app = create_app()
log_handler = logging.FileHandler("log/flask.log", encoding='utf-8')
nuc_app.logger.addHandler(log_handler)
nuc_dbc = DatabaseBzController()

register_middleware(nuc_app)

ADMINS = {
    'qwe': 'qwe',
    'admin': '12345',
    'admin1': '123451',
    'admin2': '123452'
}


#########################
# User status api       #
#########################

@nuc_app.route('/api/admin/login', methods=["POST"])
def login():
    request_data = request.get_json()
    user, pswd = request_data.get('username', ""), request_data.get('password', '')
    nuc_app.logger.info(f"receive login request {request_data}")
    if user not in ADMINS:
        status = 2
    elif ADMINS[user] != pswd:
        status = 1 
    else:
        status = 0
    
    login_data = {
        'username': user,
        'status': status
    }
    nuc_app.logger.info(f"response login data {login_data}")
    if status != 0:
        pack_error(login_data, f"err status {status}")
    return pack_response(login_data, "login sucessfully")


#########################
# Groups info           #
#########################
@nuc_app.route('/api/groups/all')
def get_all_groups():
    data = {
        "groups": nuc_dbc.getAllGroups(None),
    }
    return pack_response(data, "get groups successful")


@nuc_app.route('/api/groups/page')
def get_page_groups():
    nuc_app.logger.info(f"receive login request {request.args}")
    # request_data = request.json
    page_num = request.args.get('pageNum', '0')
    page_size = request.args.get('pageSize', '1')
    sort_with = request.args.get('sortBy')
    sort_order = request.args.get('order', 'desc')   
    page_num = int(page_num)
    page_size = int(page_size)
    groups, total = nuc_dbc.getPageGroups(page_num, page_size, sort_with, sort_order)
    data = {
        "groups": groups,
        "total": total
    }
    return pack_response(data, f"get groups successfully")

@nuc_app.route('/api/group/create', methods=['POST'])
def add_group():
    request_data = request.get_json()
    group = Group.parse(request_data.get('group', {}))
    group._id = "-1"
    nuc_dbc.createNewGroup(group)
    data = {
        "group": group
    }
    return pack_response(data, f"create group successfully")
    
    

@nuc_app.route('/api/group/spares', methods=['GET'])
def get_spare_members():
    members = nuc_dbc.getAllSpareMembers()
    data = {
        'spare_members': members
    }
    return pack_response(data, f"get member successfully")

@nuc_app.route('/api/group/dismiss', methods=['POST'])
def dismiss_group():
    request_data = request.get_json()
    group = Group.parse(request_data.get('group', {}))
    nuc_dbc.dismissGroup(group)
    return pack_response({}, f"delete group")
    
@nuc_app.route('/api/group/modifymembers', methods=['POST'])
def modify_group_members():
    request_data = request.get_json()
    query_group: Group = Group.parse(request_data.get('group', {}))
    group = nuc_dbc.getGroup(query_group)
    
    query_member_nums = list(map(lambda x: x.num, query_group.members))
    member_nums = list(map(lambda x: x.num, group.members))
    # print(f"expect {query_group}, {query_member_nums}")
    # print(f"current {group}, {member_nums}")
    
    adding_members = list(filter(lambda x: x.num not in member_nums, query_group.members))
    # print(f'adding {adding_members}')
    removing_members = list(filter(lambda x: x.num not in query_member_nums, group.members))
    # print(f"removing {removing_members}")
    nuc_dbc.addMembersToGroup(adding_members, group)
    nuc_dbc.removeMembersFromGroup(removing_members, group)
    return pack_response({}, f"members modified successfully")
    

@nuc_app.route('/api/group/modifyscore', methods=['POST'])
def modify_group_score():
    request_data = request.get_json()
    query_group: Group = Group.parse(request_data.get('group', {})) 
    group = nuc_dbc.getGroup(query_group)
    if group is not None:
        nuc_dbc.updateGroupScore(query_group)
    return pack_response({}, f"scores modified successfully")

if __name__ == '__main__':        
    nuc_app.run(port=8080, host='172.24.43.114', debug=True)