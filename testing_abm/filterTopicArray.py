import json

# Load your data (replace with your actual filename if needed)
with open("filtered_topics.json", "r") as file:
    data = json.load(file)

# Extract only topic_id values
topic_ids = [item["topic_id"] for item in data]

# Print or use the array as needed
print(topic_ids)

