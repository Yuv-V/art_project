from flask import Flask
import requests


app = Flask(__name__)

@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    # info = requests.get('http://localhost:5000/hello/'+name)
    # hello_dict = json.loads(str(info))
    info = requests.get("http://localhost:5000/hello/"+name).json()
    return info['result']


@app.route('/', methods=['GET'])
def index():
    return "helloworld"  

@app.route('/artists', methods=['GET'])
def artists():
    info = requests.get("http://localhost:5000/artists").json()
    artists = info['data']['artists']
    print(artists)
    returnString = ''
    for a in artists:
         print(a['name'])
         returnString += a['name'] + '<br/>'

    return returnString

@app.route('/art', methods=['GET'])
def art():
    info = requests.get("http://localhost:5000/art").json()
    artists = info['data']['arts']
    print(artists)
    returnString = ''
    for a in artists:
         print(a['name'])
         imgurl = a["image_url"]
         img = f'<img src="{imgurl}">'
         name = a['name'] 
         returnString += img+name+'<br/>'
    
    return returnString





if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5001)