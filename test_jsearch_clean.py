import os
import requests
from dotenv import load_dotenv

load_dotenv()
RAPIDAPI_KEY = os.getenv("JSEARCH_API_KEY")

if not RAPIDAPI_KEY:
    raise RuntimeError("JSEARCH_API_KEY not set in .env file")

url = "https://jsearch.p.rapidapi.com/search"
querystring = {"query": "Python developer", "page": "1", "num_pages": "1"}

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()

for job in data.get("data", []):
    print(f"Title: {job['job_title']}")
    print(f"Company: {job['employer_name']}")
    print(f"Location: {job['job_city']}, {job['job_country']}")
    print(f"Link: {job['job_apply_link']}")
    print("-" * 50)
