import requests

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    for post in posts:
        print(post)