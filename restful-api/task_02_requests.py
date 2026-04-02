#!/usr/bin/python3
"""
Module for fetching and processing posts from JSONPlaceholder API
"""

import requests
import csv

# API endpoint
URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts from JSONPlaceholder and print their titles.
    """
    response = requests.get(URL)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get("title"))
    else:
        print("Failed to fetch posts.")


def fetch_and_save_posts():
    """
    Fetch all posts from JSONPlaceholder and save them to posts.csv.
    """
    response = requests.get(URL)

    if response.status_code == 200:
        posts = response.json()

        # Keep only required fields
        structured_posts = [
            {
                "id": post.get("id"),
                "title": post.get("title"),
                "body": post.get("body")
            }
            for post in posts
        ]

        # Write to CSV
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as file:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(structured_posts)

        print("Posts saved to posts.csv successfully.")
    else:
        print("Failed to fetch posts.")


# Run functions if file is executed directly
if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()