import requests
from datetime import datetime
import time
import os
import markdownify


with open("cookie_topics.txt", "r") as file:
    cookie_topic = file.read().strip()


start_date = datetime(2025, 1, 1)
end_date = datetime(2025, 4, 14)


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError:
        return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


def fetch_topics(start_date, end_date):
    headers = {"Cookie": cookie_topic, "Accept": "application/json"}

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
#
#
#

with open("cookie_posts.txt", "r") as file:
    cookie_post = file.read().strip()


def fetch_topic_posts(topic_id, cookies=cookie_post):
    """
    Fetch all posts from a Discourse topic, handling pagination
    Returns list of posts in markdown format with metadata
    """
    base_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}.json"
    headers = {"cookie": cookies} if cookies else {}

    all_posts = []
    page = 1

    while True:
        response = requests.get(f"{base_url}?page={page}", headers=headers)
        if response.status_code != 200:
            print(
                f"Failed to fetch page {page} for topic {topic_id}: {response.status_code}"
            )
            break

        data = response.json()
        posts = data.get("post_stream", {}).get("posts", [])

        if not posts:
            break

        for post in posts:
            # Convert HTML content to markdown
            html_content = post.get("cooked", "")
            markdown_content = markdownify.markdownify(html_content)

            # Store relevant post information
            post_data = {
                "id": post["id"],
                "topic_id": topic_id,
                "topic_title": data.get("title", ""),
                "username": post.get("username", ""),
                "created_at": post.get("created_at", ""),
                "content": markdown_content,
                "url": f"https://discourse.onlinedegree.iitm.ac.in/t/{data.get('slug', '')}/{topic_id}/{post.get('post_number', '')}",
                "tags": data.get("tags", []),
                "post_number": post.get("post_number", 0),
            }
            all_posts.append(post_data)

        page += 1
        time.sleep(0.3)  # Respectful delay to avoid overwhelming the server

    return all_posts


def save_topic_to_markdown(topic_id, cookies=None):
    """
    Fetch all posts from a topic and save them to a markdown file
    """
    posts = fetch_topic_posts(topic_id, cookies)
    if not posts:
        print(f"No posts found for topic {topic_id}")
        return

    # Get topic info from first post
    topic_title = posts[0]["topic_title"]
    tags = posts[0]["tags"]
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create filename (sanitize title)
    filename = (
        f"topic_{topic_id}_{topic_title[:50].replace(' ', '_').replace('/', '-')}.md"
    )

    # Create discourse folder if it doesn't exist
    os.makedirs("discourse", exist_ok=True)
    filepath = os.path.join("discourse", filename)

    with open(filepath, "w", encoding="utf-8") as md_file:
        # Write header
        md_file.write(f"# {topic_title}\n\n")
        md_file.write(f"- **Topic ID**: {topic_id}\n")
        md_file.write(f"- **Tags**: {', '.join(tags)}\n")
        md_file.write(f"- **Saved on**: {created_at}\n")
        md_file.write(
            f"- **Original URL**: {posts[0]['url'].split('/')[0]}/t/{posts[0]['url'].split('/')[-3]}\n"
        )
        md_file.write(f"- **Total posts**: {len(posts)}\n\n")
        md_file.write("---\n\n")

        # Write each post
        for post in posts:
            md_file.write(f"## Post #{post['post_number']}\n\n")
            md_file.write(f"- **Author**: {post['username']}\n")
            md_file.write(f"- **Posted on**: {post['created_at']}\n")
            md_file.write(f"- **URL**: {post['url']}\n\n")
            md_file.write(post["content"])
            md_file.write("\n\n---\n\n")

    print(f"Successfully saved {len(posts)} posts to {filepath}")


# Example usage

for i in range(3):
    topic = all_topic_ids[i]
    save_topic_to_markdown(topic, cookies=cookie_post)
