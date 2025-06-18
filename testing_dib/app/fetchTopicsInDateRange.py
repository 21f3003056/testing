import requests
from datetime import datetime


with open("cookie_topics.txt", "r") as file:
    cookie = file.read().strip()


start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 4, 14)


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


def fetch_topics(start_date, end_date):
    headers = {"Cookie": cookie, "Accept": "application/json"}

    base_url = "https://discourse.onlinedegree.iitm.ac.in/search?q=%23courses%3Atds-kb%20after%3A2025-01-01%20order%3Aviews"
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
        if "topics" not in data or not data["topics"]:
            break
        for topic in data["topics"]:
            created_at = parse_date(topic["created_at"])
            if start_date <= created_at <= end_date:
                if topic["id"] not in all_topics:
                    all_topics.append(topic["id"])
        page += 1

    return all_topics


all_topic_ids = fetch_topics(start_date, end_date)

print(all_topic_ids)
