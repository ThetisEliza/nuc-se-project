from flask import Flask,  Response, request, abort

def register_middleware(app: Flask):
    
    @app.before_request
    def before_request_test():
        pass
        
    @app.after_request
    def after_request_test(response: Response) -> Response:
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Method'] = '*'
        response.headers['Access-Control-Allow-Headers'] = '*'
        if request.method == "OPTION":
            abort(200)
        return response
        