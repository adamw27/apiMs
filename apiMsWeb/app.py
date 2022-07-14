from flask import Flask, render_template, redirect, url_for, request, flash
import requests

url = 'https://jsonplaceholder.typicode.com'

app = Flask(__name__)
app.secret_key = "secretkey"

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        if request.form.get("get") == "GET":
            user_id = request.form["userId"]
            post_id = request.form["postId"]
            title = request.form["title"]
            body = request.form["body"]
            if post_id == 0:
                response = requests.get(f"{url}/posts")
            elif post_id >= 1 or post_id <= 100:
                response = requests.get(f"{url}/posts/{post_id}")
            else:
                return render_template('index.html')
            return response.text
        elif request.form.get("post") == "POST":
            user_id = request.form["userId"]
            post_id = request.form["postId"]
            title = request.form["title"]
            body = request.form["body"]
            user_valid = requests.get(f"{url}/users/{user_id}")
            if user_valid.status_code == 200:
                post_new = {
                    "userId": user_id,
                    "id": None,
                    "title": title,
                    "body": body
                }
                response = requests.post(f"{url}/posts", json=post_new)  # posting a new post
            else:
                return render_template('index.html')
            return response.text
        elif request.form.get("put") == "PUT":
            user_id = request.form["userId"]
            post_id = request.form["postId"]
            title = request.form["title"]
            body = request.form["body"]
            user_valid = requests.get(f"{url}/users/{user_id}")
            if user_valid.status_code == 200:
                post_updated = {
                    "userId": user_id,
                    "id": None,
                    "title": title,
                    "body": body
                }
                response = requests.put(f"{url}/posts/{post_id}", json=post_updated)  # to update a post
            else:
                return render_template('index.html')
            return response.text
        elif request.form.get("delete") == "DELETE":
            user_id = request.form["userId"]
            post_id = request.form["postId"]
            title = request.form["title"]
            body = request.form["body"]
            response = requests.delete(f"{url}/posts/{post_id}")  # print(response.status_code) to see if it got deleted
            return str(response.status_code)
        else:
            return render_template('index.html')
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
