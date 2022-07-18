import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
import requests
url = 'https://jsonplaceholder.typicode.com'


def req_fun():
    request = input("Pick a request GET/POST/PUT/DELETE: ").upper()
    if request == "GET":
        get()
    elif request == "POST":
        post()
    elif request == "PUT":
        put()
    elif request == "DELETE":
        delete()
    else:
        invalid_input()


def get():
    user_or_post = str(input("For all posts made by a user enter 'user' or to find a post by an ID enter 'id': "))
    if user_or_post == "user":
        user_id = int(input("Enter the UserID: "))
        user_valid = requests.get(f"{url}/users/{user_id}")
        if user_valid.status_code == 200:
            post_id = (user_id * 10) - 10
            for i in range(post_id + 1, post_id + 11):
                print(requests.get(f"{url}/posts/{i}").status_code)
                print(requests.get(f"{url}/posts/{i}").text)
            req_fun()
        else:
            print("The user was not found.")
            invalid_input()
    elif user_or_post == "id":
        post_id = int(input("For a specific post enter an ID (1-100) or enter 0 for all: "))
        post_valid = requests.get(f"{url}/posts/{post_id}")
        if post_id == 0:
            response = requests.get(f"{url}/posts")  # get all posts
            res(response)
        elif post_valid.status_code == 200:
            response = requests.get(f"{url}/posts/{post_id}")  # get a specific post
            res(response)
        else:
            print("The post was not found.")
            invalid_input()
    else:
        invalid_input()


def post():
    user_id = int(input("Enter your UserID: "))
    user_valid = requests.get(f"{url}/users/{user_id}")
    if user_valid.status_code == 200:
        title_new = str(input("Enter the title: "))
        body_new = str(input("Enter the body: "))
        post_new = {
            "userId": user_id,
            "id": None,
            "title": title_new,
            "body": body_new
        }
        response = requests.post(f"{url}/posts", json=post_new)  # posting a new post
        res(response)
    else:
        print("The user was not found.")
        invalid_input()


def put():
    post_id = int(input("Enter ID of the post to update: "))
    if 1 <= post_id <= 100:
        user_updated = int(input("Enter your UserID: "))
        user_valid = requests.get(f"{url}/users/{user_updated}")
        if user_valid.status_code == 200:
            title_updated = str(input("Enter the new title: "))
            body_updated = str(input("Enter the new body: "))
            post_updated = {
                "userId": user_updated,
                "id": None,
                "title": title_updated,
                "body": body_updated
            }
            response = requests.put(f"{url}/posts/{post_id}", json=post_updated)  # to update a post
            res(response)
        else:
            print("The user was not found.")
            invalid_input()
    else:
        print("The post was not found.")
        invalid_input()


def delete():
    post_id = int(input("Enter ID of the post to delete: "))
    post_valid = requests.get(f"{url}/posts/{post_id}")
    if post_valid.status_code == 200:
        response = requests.delete(f"{url}/posts/{post_id}")  # print(response.status_code) to see if it got deleted
        res(response)
    else:
        print("The post was not found.")
        invalid_input()


def res(response):
    print(response.status_code)
    print(response.text)
    req_fun()


def invalid_input():
    print("Invalid input.")
    req_fun()


req_fun()
