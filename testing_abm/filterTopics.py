import json
from datetime import datetime

# Load your data (replace with your actual filename if needed)
with open("discourseTopics.json", "r") as file:
    data = json.load(file)

# Define date range (inclusive)
start_date = datetime.fromisoformat("2025-01-01T00:00:00.000Z".replace("Z", "+00:00"))
end_date = datetime.fromisoformat("2025-04-14T23:59:59.999Z".replace("Z", "+00:00"))

# Filter the data
filtered = [
    item for item in data
    if start_date <= datetime.fromisoformat(item["created_at"].replace("Z", "+00:00")) <= end_date
]

# Save the filtered data
with open("filtered_topics.json", "w") as file:
    json.dump(filtered, file, indent=4)

print("Filtered topics written to filtered_output.json")
