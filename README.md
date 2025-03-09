# Goodreads Genre-Based Book Scraper

## 📌 Overview
This project is a web scraper that extracts book data from Goodreads based on different genres. It collects details such as:
- **Title**
- **Author**
- **Average Rating**
- **Total Ratings**
- **Year Published**
- **Book Cover Image URL**

The scraped data is saved into a CSV file for further analysis.

## ⚙️ Technologies Used
- **Python**
- **Selenium**
- **BeautifulSoup**
- **Pandas**
- **Regex**

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
📂 goodreads-scraper
├── 📄 scraper.py          # Main scraping script
├── 📄 requirements.txt    # List of dependencies
├── 📄 README.md           # Documentation
└── 📄 goodreads_books_by_genre.csv  # Output file (generated)
```

## 📝 Notes
- The scraper uses a **headless** Chrome browser for automation.
- To avoid getting blocked, the script includes a **5-second delay** before extracting data.
- Goodreads might update its site structure, so ensure the **CSS selectors** are up to date.

## 📌 To-Do
- [ ] Implement multi-threading for faster scraping
- [ ] Add support for paginated results
- [ ] Improve error handling

## 🤝 Contributions
Feel free to fork the repo, submit PRs, or open issues! 😊