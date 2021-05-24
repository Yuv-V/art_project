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
	"artists": [{
			"id": 0,
			"name": "Todd Crosby" 
		},
		{
			"id": 1,
			"name": "Benton Page"
		},
		{
			"id": 2,
			"name": "Lowe Whitfield"
		}
	]
}
    return jsonify({'data': artists})

@app.route('/art', methods=['GET'])
def art():
    art = {
	"arts": [{
			"id": 0,
			"name": "Todd Crosby", 
			"image_url": "http://lorempixel.com/400/200/sports/1/" 
		},
		{
			"id": 1,
			"name": "Benton Page",
			"image_url": "http://lorempixel.com/400/200/sports/2/" 
		},
		{
			"id": 2,
			"name": "Lowe Whitfield",
			"image_url": "http://lorempixel.com/400/200/sports/3/" 
		}
	]
}
    return jsonify({'data': art})



if __name__ == '__main__':
    app.run(debug=True)


