from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'result': 'hello'})

@app.route('/hello/<name>', methods=['GET'])
def helloname(name):
    return jsonify({'result': 'hello world  '+name})



if __name__ == '__main__':
    app.run(debug=True)


