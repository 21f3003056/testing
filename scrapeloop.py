# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
import json

with open("cookiesOne.txt", "r") as file:
    cookie = file.read().strip()

headers = {
    "cookie":cookie
}

topic_id = 164277
base_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}.json"
all_posts = []
page = 1

while True:
    response = requests.get(f"{base_url}?page={page}", headers=headers)
    if response.status_code == 404:
        break
    data = response.json()
    print(data)
    all_posts.extend(data['post_stream']['posts'])
    page += 1

with open ("discourseScrape.json", "w") as file:
    json.dump(all_posts, file, indent=4)