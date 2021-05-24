from flask import Flask
from flask import request
from flask import jsonify


app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({'result': 'hello'})

@app.route('/hello/<name>', methods=['GET'])
def helloname(name):
    return jsonify({'result': 'hello  '+name})

@app.route('/artists', methods=['GET'])
def artists():
    artists = {
	"art": [{
			"id": 0,
			"name": "Woods" 
		},
		{
			"id": 1,
			"name": "Guitar"
		},
		{
			"id": 2,
			"name": "Galaxy"
		}
	]
}
    return jsonify({'data': artists})



if __name__ == '__main__':
    app.run(debug=True)