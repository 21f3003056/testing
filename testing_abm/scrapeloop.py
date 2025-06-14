# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests<3",
#   "rich",
# ]
# ///

import requests
import json
from pprint import pprint

with open("cookiesPost.txt", "r") as file:
    cookie = file.read().strip()

headers = {
    "cookie":cookie
}

topicIDs = [164277, 169029, 171141, 161083, 165959, 163247, 168832, 161120, 166576, 172333, 168449, 172246, 168476, 169283, 168916, 171668, 169888, 168506, 166866, 169045, 167344, 170413, 161071, 171798, 166816, 171054, 169369, 170147, 171477, 161214, 168384, 168458, 168142, 164214, 172254, 168567, 165687, 166189, 171672, 165396, 171428, 168901, 164147, 163147, 163381, 171500, 166593, 171485, 163158, 168537, 172471, 172546, 163241, 166303, 167471, 169807, 171541, 161072, 171999, 168943, 165433, 164291, 171422, 171525, 170309, 167415, 168303, 167878, 163765, 168011, 168482, 172021, 172373, 168825, 166498, 172497, 167172, 170131, 168987, 168515, 166738, 171473, 166891, 164869, 164462, 169247, 167410, 164737, 163144, 169352, 162425, 168310, 164089, 164205, 167072, 167679, 165416, 165746, 165142, 166651, 168143, 163224, 169393, 166100, 164460, 168057, 165593, 168017, 166349, 167699, 165922, 166634, 165830, 169456, 166357, 171515, 166647]
topic_id = 164277
base_url = f"https://discourse.onlinedegree.iitm.ac.in/t/{topic_id}.json"
all_posts = []
page = 1

while True:
    response = requests.get(f"{base_url}?page={page}", headers=headers)
    if response.status_code == 404:
        break
    data = response.json()
    # all_posts.extend(data['post_stream']['posts'])
    # all_posts.extend(response)
    result = json.dumps(data, indent=4)
    print(result)
    page += 1
    break

# with open ("discourseScrapeFull.json", "w") as file:
    # json.dump(all_posts, file, indent=4)