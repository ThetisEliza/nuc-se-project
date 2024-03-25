
from flask import jsonify, Response, abort

__SUCC_CODE = 200
__ERR_CODE = 301

_CODE = "code"
_MSG = 'msg'

def pack_response(data: dict, msg: str) -> Response:
    data = {
        **data,
        _MSG: msg,
        _CODE: __SUCC_CODE
    }
    return jsonify(data)

def pack_error(data: dict, msg: str):
    data = {
        **data,
        _MSG: msg,
        _CODE: __ERR_CODE
    }
    abort(jsonify(data))
    