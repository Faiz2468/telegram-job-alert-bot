import os
import requests
from dotenv import load_dotenv

# Load .env file
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

print(response.json())