"""
main.py
Entry point for the AI News Email Agent.
"""

from config import validate_config

from news.fetch_news import fetch_latest_news
from ai.summarize import summarize_articles
from email.email_template import generate_email_html
from email.send_email import send_email


def main():
    print("=" * 60)
    print("AI News Email Agent Started")
    print("=" * 60)

    # Validate configuration
    validate_config()

    print("\nFetching latest news...")
    articles = fetch_latest_news()

    if not articles:
        print("No news articles found.")
        return

    print(f"Fetched {len(articles)} articles.")

    print("\nGenerating AI summaries...")
    summarized_articles = summarize_articles(articles)

    print("\nCreating HTML email...")
    email_body = generate_email_html(summarized_articles)

    print("\nSending email...")
    send_email(
        subject="📰 Daily AI News Digest",
        html_body=email_body
    )

    print("\nEmail sent successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
