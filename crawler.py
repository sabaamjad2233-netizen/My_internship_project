import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def start_crawling(start_url):
    current_url = start_url
    all_posts = []       
    seen_titles = set()  
    page_number = 1
    
    while current_url:
        print(f"Hum Page number {page_number} ko read kar rahe hain...")
        response = requests.get(current_url)
        if response.status_code != 200:
            print("Oh ho! Page nahi khul raha.")
            break
            
        soup = BeautifulSoup(response.text, 'html.parser')
        posts_on_page = soup.find_all('div', class_='quote')
        
        if not posts_on_page:
            print("Is page par koi post nahi mili.")
            break
            
        for post in posts_on_page:
            text_element = post.find('span', class_='text')
            text = text_element.text.strip() if text_element else "Missing Text"
            
            author_element = post.find('small', class_='author')
            author = author_element.text.strip() if author_element else "Unknown Author"
            
            if text in seen_titles:
                continue
                
            seen_titles.add(text)
            all_posts.append({'Text': text, 'Author': author})
            
        next_button = soup.find('li', class_='next')
        if next_button and next_button.find('a'):
            next_page_url = next_button.find('a')['href']
            current_url = "https://quotes.toscrape.com" + next_page_url
            page_number += 1
            time.sleep(1) 
        else:
            current_url = None
            print("Saare pages khatam ho gaye!")
            
    if all_posts:
        df = pd.DataFrame(all_posts)
        df.to_csv('forum_posts.csv', index=False)
        print("\nMubarak ho! 'forum_posts.csv' file ban gayi hai.")

if __name__ == "__main__":
    target_url = "https://quotes.toscrape.com/" 
    start_crawling(target_url)