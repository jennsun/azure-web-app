from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='client/build', static_url_path='/')

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')
