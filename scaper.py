import requests
from bs4 import BeautifulSoup

import time

# Base URL for page 1
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page = 1

while True:
    time.sleep(1) # Wait for 1 second between requests
    
    # Request each page and set encoding
    response = requests.get(base_url.format(page))
    response.encoding = 'utf-8'  # Ensure UTF-8 encoding
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find book elements
    books = soup.find_all('article', class_='product_pod')
    
    # If no books are found, exit the loop (reached the end of pages)
    if not books:
        break
    
    # Extract and print information for each book
    for book in books:

        title = book.h3.a['title']  # Title is within <a> inside <h3>
        
        price = book.find('p', class_='price_color').text.strip()  # Price is within <p> with class price_color
        
        # Find the rating element within each book
        rating_class = book.find('p', class_='star-rating')['class']  # This gets the list of classes for the rating <p> tag
        rating = rating_class[1]  # The second class (e.g., 'Three') indicates the rating
        if rating == 'One':
            rating = 1
        elif rating == 'Two':
            rating = 2
        elif rating == "Three":
            rating = 3
        elif rating == "Four":
            rating = 4
        elif rating == 5:
            rating = 5

        
        print(f"Title: {title}\nRating: {rating} stars\nPrice: {price}\n")
    
    # Go to the next page
    page += 1

