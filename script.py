import json
import requests

response = requests.get("https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/course-rag-movies.json")
data = response.json()

with open("data/movies.json", "w") as f:
    json.dump(data, f, indent=4)