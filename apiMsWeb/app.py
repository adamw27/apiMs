import os
from turtle import title
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import requests

url = 'https://jsonplaceholder.typicode.com'

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Post(db.Model):
    postId = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    title = db.Column(db.String(100), nullable=False)
    body = db.Column(db.Text, nullable=False)

@app.route('/')
def index():
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>/')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        userId = int(request.form['userId'])
        title = request.form['title']
        body = request.form['body']
        post = Post(userId=userId,
                    title=title,
                    body=body)
        user_valid = requests.get(f"{url}/users/{userId}")
        if user_valid.status_code == 200:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

    return render_template('create.html')

@app.route('/<int:post_id>/edit/', methods=('GET', 'POST'))
def edit(post_id):
    post = Post.query.get_or_404(post_id)

    if request.method == 'POST':
        postId = int(request.form['postId'])
        userId = int(request.form['userId'])
        title = request.form['title']
        body = request.form['body']

        post.postId = postId
        post.userId = userId
        post.title = title
        post.body = body

        user_valid = requests.get(f"{url}/users/{userId}")
        if user_valid.status_code == 200:
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)

@app.route('/<int:post_id>/delete/', methods=["POST"])
def delete(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('index'))
