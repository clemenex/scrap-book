# Goodreads Genre-Based Book Scraper

## ⚠ WARNING ⚠
The Dockerfile and container initialization are a current work in progress and is currently not working. For the current status of the project, please refer to the `book.py` only.

## 📌 Overview
This project is a web scraper that extracts book data from Goodreads based on different genres. It collects details such as:
- **Title**
- **Author**
- **Average Rating**
- **Total Ratings**
- **Year Published**
- **Book Cover Image URL**

The scraped data is saved into a CSV file for further analysis. The types of data gathered are all relevant to building a much larger project later on. This data will be used to build a Genre-based Book Recommendation System using Machine Learning and Deep Learning Techniques.

## 🌐 Website Selection
### GoodReads
URL: https://www.goodreads.com

I chose this website because it is one of the open source book websites that allow web scraping. More specifically, although scraping from `/search` is not allowed, I can scrape data just from `/shelf/show` as it was neither indicated as disallow or allow in the `robots.txt`. Because of this, I can the set the scraping URL to `/shelf/show/(insert specific genre)`. 

## ⚙️ Technologies Used
- **Python**
- **Selenium**
- **BeautifulSoup**
- **Pandas**
- **Regex**

## 📋 Challenges and Limitations
### 1️⃣ Dynamic Content
The website uses JavaScript to dynamically load its content. Because of this, I had to use another scraping tool, `Selenium` in order to handle dynamic content, on top of `BeautifulSoup`. Selenium is used to automate a real browser session, which can process JavaScript and dynamically load content. By using driver.get(genre_url), the script allows the browser to fully load the page, including any JavaScript-rendered elements, before scraping the data. After waiting for the page to load (time.sleep(5)), the script fetches the fully rendered HTML with driver.page_source. This ensures that the book data, which is dynamically loaded by JavaScript, is available for scraping.

### 2️⃣ Anti-Scraping Measures
Websites like Goodreads often implement anti-scraping measures to prevent bots from overwhelming their servers or to protect their data. These measures may include:

- Rate limiting (e.g., limiting the number of requests per minute).
- Blocking IP addresses that make too many requests in a short period.
- CAPTCHA challenges.

How I addressed this:

- **Headless Mode**: By running the browser in headless mode (without opening the actual browser window), the script mimics human browsing behavior and reduces the chances of detection by the site.
- **User-Agent**: The script sets a custom user-agent header ("user-agent=Mozilla/5.0..."), which helps in simulating requests from a standard web browser rather than a bot.
- **Delays between requests**: The script uses time.sleep(5) to pause for a few seconds between scraping different pages. This prevents the script from sending requests too quickly, which is a common sign of scraping activity.

### 3️⃣ Extracting and Parsing Data
Scraping data from dynamic pages often results in dealing with complex and inconsistent HTML structures. Identifying the correct HTML tags and classes that contain the data you want to scrape can be challenging, as even minor changes to the website’s layout can break the script.

How I addressed this:

- **BeautifulSoup**: BeautifulSoup is used to parse the HTML page and extract the required information. The script searches for specific tags with known classes (class_="elementList", class_="bookTitle", etc.), which are consistent for each book entry.
- **Regular Expressions**: Regular expressions are used to extract specific pieces of text from the book’s metadata (e.g., average rating, number of ratings, year published) embedded in the page text.

## ✅ Ethical Considerations
The project follows the rules and guidelines laid down by the website (https://www.goodreads.com/robots.txt). No personal data such as `user-shelf` or specific book data from `/search` was scraped in order to avoid breaking the scraping guidelines.

- The project avoids scraping any personal or sensitive information and only collects publicly available data such as book titles, authors, ratings, genres, and publication years.
- Personal details such as user reviews, profile data, or private messages are not scraped. The script is focused solely on general book data from the public genre pages.
- The script uses a delay (time.sleep(5)) between each request to reduce the load on the server and mimic more human-like browsing behavior. This prevents overwhelming Goodreads’ servers with too many rapid requests. By scraping at a controlled rate, the script aims to prevent affecting the user experience of others and to avoid violating terms related to server load or overuse.

## 📁 Output and Result
For the project's output and result, kindly refer and open the csv file: `goodreads_books_by_genre.csv`. The file can be viewed by itself here on Github or may also be downloadable.

## 🚀 How to Run the Scraper
### 1️⃣ Install Dependencies
Ensure you have Python installed, then install the required packages:
```sh
pip install selenium beautifulsoup4 pandas webdriver-manager
```

### 2️⃣ Run the Script
Execute the following command:
```sh
python scraper.py
```

The scraper will fetch book details from multiple Goodreads genres and save them in `goodreads_books_by_genre.csv`.

## 📁 Project Structure
```
📂 scrap-book
├── 📄 book.py          # Main scraping script
├── 📄 README.md           # Documentation
└── 📄 goodreads_books_by_genre.csv  # Output file (generated)
```

## 📝 Notes
- The scraper uses a **headless** Chrome browser for automation.
- To avoid getting blocked, the script includes a **5-second delay** before extracting data.
- Goodreads might update its site structure, so ensure the **CSS selectors** are up to date.

## 📌 To-Do
- [ ] Finish docker containerization setup
- [ ] Add airflow to automate scraping
- [ ] Setup airflow DAGs

## 🤝 Contributions
Feel free to fork the repo, submit PRs, or open issues! 😊