from flask import Flask, session, render_template, request, redirect, g, url_for
from jinja2 import Template
#from pymongo import MongoClient

import os
app = Flask(__name__)

app.secret_key = os.urandom(24)

#client = MongoClient("mongodb+srv://dbYuv:yuv12345@cluster0.eqja2.mongodb.net/art?retryWrites=true&w=majority")

#db = client['art']

#db.users.insert({"Yuv": "yuv12345"})

@app.route('/login')
def login():
     return render_template('login.html')

@app.route('/page1')
def page1():
     return render_template('page1.html')

@app.route('/page2')
def page2():
     return render_template('page2.html')

@app.route('/')
def index():
    return render_template('blog.html')

@app.route('/blog1')
def blog1():
    return render_template('blog1.html')

@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/gallery')
def gallery():
    return render_template('gallery2.html')

@app.route('/edit')
def edit():
    return render_template('edit.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         session.pop('user', None)

#         if request.form['password'] == 'password' and request.form['username'] == 'Yuv':
#             session['user'] = request.form['username']
#             return redirect(url_for('protected'))
#         else:
#             return render_template("login.html", ver="Invalid credentials!")
#     return render_template('login.html')
        
# @app.route("/signup")
# def signup():
#     return render_template("login.html", ver="Account created!")

# @app.route('/protected')
# def protected():
#     if g.user:
#         return render_template('secure.html', user=session['user'])
#     return render_template("login.html", ver="Remeber to login!")

# @app.before_request
# def before_request():
#     g.user = None

    # if 'user' in session:
    #     g.user = session['user']

# @app.route('/dropsession')
# def dropsession():
#     session.pop('user', None)
#     return render_template('app.html')

if __name__ == "__main__":
    app.run(debug=True)