import requests

API_KEY = "37407b88f40d4ab89f9978983da48712"

url = f"https://newsapi.org/v2/everything?q=artificial intelligence&apiKey={API_KEY}"

response = requests.get(url)

data = response.json()

articles = data["articles"]

with open("news.txt", "w", encoding="utf-8") as file:

    for article in articles[:5]:

        file.write(article["title"] + "\n")
import os
import requests
import smtplib

from email.mime.text import MIMEText
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

client = OpenAI(api_key=OPENAI_API_KEY)

url = (
    f"https://newsapi.org/v2/everything?"
    f"q=artificial intelligence&"
    f"language=en&"
    f"sortBy=publishedAt&"
    f"apiKey={NEWS_API_KEY}"
)

response = requests.get(url)

articles = response.json()["articles"][:5]

news_text = ""

for article in articles:
    title = article["title"]
    description = article["description"]

    news_text += f"\nTitle: {title}\n"
    news_text += f"Description: {description}\n"

prompt = f"""
Summarize the following AI news into a concise email digest.

{news_text}
"""

summary = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

email_body = summary.choices[0].message.content

msg = MIMEText(email_body)

msg["Subject"] = "Daily AI News Digest"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()

server.login(
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)

server.send_message(msg)

server.quit()

print("Email sent successfully!")
