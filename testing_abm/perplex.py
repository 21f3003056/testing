# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
import json

with open("cookiesTopic.txt", "r") as file:
    cookie = file.read().strip()

headers = {
    "Cookie": cookie,
    "Accept": "application/json"
}

base_url = "https://discourse.onlinedegree.iitm.ac.in/search.json?q=%23courses%3Atds-kb%20after%3A2025-01-01%20order%3Aviews"
all_topics = []
page = 1

while True:
    response = requests.get(f"{base_url}&page={page}", headers=headers)
    if response.status_code == 404:
        break
    if "application/json" not in response.headers.get("Content-Type", ""):
        print(f"Non-JSON response received (status {response.status_code}):")
        print(response.text[:500])  # Print first 500 chars for debugging
        break
    data = response.json()
    if 'topics' not in data or not data['topics']:
        break
    for topic in data['topics']:
        all_topics.append({
            "topic_id": topic['id'],
            "created_at": topic['created_at']
        })
    page += 1

with open("discourseTopics.json", "w") as file:
    json.dump(all_topics, file, indent=4)
