import requests
from bs4 import BeautifulSoup
from src.database import get_connection

def fetch_sample_data():
    # Sample real-world simulated crawler logic
    sample_posts = [
        ("web", "The new upgrade is fantastic! Super fast and accurate."),
        ("web", "Terrible experience, the application crashes constantly."),
        ("web", "Customer support was decent, resolved my issue quickly."),
        ("web", "Worst service ever, highly disappointed with the quality."),
        ("web", "Great tool for daily workflow, saves a lot of time!")
    ]
    return sample_posts

def run_crawler():
    posts = fetch_sample_data()
    conn = get_connection()
    cursor = conn.cursor()
    
    for source, text in posts:
        cursor.execute(
            "INSERT INTO posts (source, raw_text, processed_flag) VALUES (?, ?, 0)",
            (source, text)
        )
    conn.commit()
    conn.close()
    return f"Crawled and stored {len(posts)} posts."

if __name__ == "__main__":
    print(run_crawler())