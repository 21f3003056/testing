import requests

with open("cookie_topics.txt", "r") as file:
    cookie = file.read().strip()


def fetch_topics_via_search(start_date, end_date, cookies=cookie):
    """
    Fetch topics using the search API which might have different permissions
    """
    base_url = "https://discourse.onlinedegree.iitm.ac.in/search.json"
    headers = {"cookie": cookies} if cookies else {}
    all_topics = []
    page = 0

    while True:
        # Search for topics in category 34 within date range
        query = {"q": f"before:{end_date} after:{start_date} category:34", "page": page}
        response = requests.get(base_url, headers=headers, params=query)

        if response.status_code != 200:
            print(f"Failed to fetch page {page}: {response.status_code}")
            print(response.text)
            break

        data = response.json()
        topics = data.get("topics", [])

        if not topics:
            break

        for topic in topics:
            all_topics.append(topic["id"])

        page += 1

    return sorted(all_topics)


# Test the search API approach
topic_ids = fetch_topics_via_search(
    start_date="2025-01-01", end_date="2025-04-14", cookies=cookie
)
print(f"Found {len(topic_ids)} topics via search API")
print(f"topic_ids: {topic_ids}")  # Print first 10 topic IDs for verification
