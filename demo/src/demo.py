from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'welcome to my webpage!'

if __name__ == '__main__':
    app.run(port=8080, host='172.24.43.114', debug=True)