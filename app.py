import requests
from openai import OpenAI

NEWS_API_KEY = "YOUR_API_KEY"

url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={NEWS_API_KEY}"

response = requests.get(url)
articles = response.json()["articles"][:5]

for article in articles:
    print(article["title"])
