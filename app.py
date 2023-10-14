from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='client/build', static_url_path='/')

# @app.route('/')
# def hello_world():
#     return "Hello, World!"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists("client/build/" + path):
        return send_from_directory('client/build', path)
    else:
        return send_from_directory('client/build', 'index.html')
