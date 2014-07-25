from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = { 'nickname': 'Adam' }   # fake user
    posts = [   # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'How do I use flask?'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'Is this going to appear on the web page?'
        }
    ]

    return render_template("index.html",
        title = 'Home',
        user = user,
        posts = posts)