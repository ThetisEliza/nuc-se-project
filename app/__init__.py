from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.json.ensure_ascii = False
    return app