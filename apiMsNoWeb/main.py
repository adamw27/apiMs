import requests

url = 'https://jsonplaceholder.typicode.com'
#error handling try except

def req_fun():
    request = input("Pick a request GET/POST/PUT/DELETE: ").upper()
    if request == "GET":
        user_or_post = str(input("For all posts made by a user enter 'user' or to find a post by ID enter 'id': "))
        if user_or_post == "user":
            user_id = int(input("Enter the UserID: "))
            user_valid = requests.get(f"{url}/users/{user_id}")
            if user_valid.status_code == 200:
                post_id = (user_id * 10) - 10
                for i in range(post_id + 1, post_id+11):
                    print(requests.get(f"{url}/posts/{i}").status_code)
                    print(requests.get(f"{url}/posts/{i}").text)
                req_fun()
            else:
                invalid_input()
        elif user_or_post == "id":
            post_id = int(input("For a specific post enter an ID (1-100) or enter 0 for all: "))
            if post_id == 0:
                response = requests.get(f"{url}/posts")  #get all posts
            elif post_id >= 1 or post_id <= 100:
                response = requests.get(f"{url}/posts/{post_id}")  #get a specific post
            else:
                invalid_input()
        else:
            invalid_input()
    elif request == "POST":
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
            response = requests.post(f"{url}/posts", json=post_new) #posting a new post
        else:
            invalid_input()
    elif request == "PUT":
        post_id = int(input("Enter ID of the post to update: "))
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
            response = requests.put(f"{url}/posts/55", json=post_updated)  # to update a post
        else:
            invalid_input()
    elif request == "DELETE":
        post_id = int(input("Enter ID of the post to delete: "))
        response = requests.delete(f"{url}/posts/{post_id}")  # print(response.status_code) to see if it got deleted
    else:
        invalid_input()

    print(response.status_code)
    print(response.text)
    req_fun()

def invalid_input():
    print("Invalid input.")
    req_fun()

req_fun()
