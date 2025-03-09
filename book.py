import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

genres = [
    "Art", "Biography", "Business", "Children's", "Christian", "Classics", "Comics", "Cookbooks", "Ebooks", "Fantasy",
    "Fiction", "Graphic-Novels", "Historical-Fiction", "History", "Horror", "Memoir", "Music", "Mystery", "Nonfiction",
    "Poetry", "Psychology", "Romance", "Science", "Science-Fiction", "Self-Help", "Sports", "Thriller", "Travel", "Young-Adult"
]

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

all_books = []

for genre in genres:
    genre_url = f"https://www.goodreads.com/shelf/show/{genre.lower().replace(' ', '-').replace("'", '')}"
    print(f"Scraping {genre}... ({genre_url})")
    
    driver.get(genre_url)
    time.sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    for book_div in soup.find_all("div", class_="elementList"):
        title_tag = book_div.find("a", class_="bookTitle")
        author_tag = book_div.find("a", class_="authorName")
        rating_tag = book_div.find("span", class_="greyText smallText")
        image_tag = book_div.find("a", class_="leftAlignedImage")

        title = title_tag.text.strip() if title_tag else "Unknown Title"
        author = author_tag.text.strip() if author_tag else "Unknown Author"
        image_url = image_tag["href"] if image_tag else "No Image"
        rating_text = rating_tag.get_text(" ", strip=True) if rating_tag else "No Rating Data"

        avg_rating, total_ratings, year_published = "N/A", "N/A", "N/A"

        avg_match = re.search(r"avg rating ([\d.]+)", rating_text)
        if avg_match:
            avg_rating = avg_match.group(1)

        total_ratings_match = re.search(r"([\d,]+) ratings", rating_text)
        if total_ratings_match:
            total_ratings = total_ratings_match.group(1).replace(",", "")

        year_match = re.search(r"published (\d{4})", rating_text)
        if year_match:
            year_published = year_match.group(1)

        all_books.append({
            "genre": genre,
            "title": title,
            "author": author,
            "avg_rating": avg_rating,
            "total_ratings": total_ratings,
            "year_published": year_published,
            "image_url": image_url
        })

driver.quit()

df = pd.DataFrame(all_books)
df.to_csv("goodreads_books_by_genre.csv", index=False)

print("Scraping complete! Data saved to 'goodreads_books_by_genre.csv'.")
