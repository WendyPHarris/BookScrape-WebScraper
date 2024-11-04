# Import the necessary libraries
import requests  # Used to make HTTP requests to websites
from bs4 import BeautifulSoup  # BeautifulSoup is used for parsing HTML
import time  # Provides time-related functions, here it's used to add a delay between requests

# Set the base URL for the website's catalogue pages
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
page = 1  # Start on the first page

# Start an infinite loop to go through each page
while True:
    time.sleep(1)  # Wait for 1 second between each request to avoid overloading the server
    
    # Make an HTTP GET request to fetch the content of the current page
    response = requests.get(base_url.format(page))  # `.format(page)` replaces `{}` in `base_url` with the page number
    response.encoding = 'utf-8'  # Set the response encoding to UTF-8 to handle special characters
    
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')  # 'html.parser' tells BeautifulSoup to use the built-in HTML parser
    
    # Find all book elements on the page
    books = soup.find_all('article', class_='product_pod')  # Each book is within an <article> tag with class 'product_pod'
    
    # Check if there are no books found (end of pages)
    if not books:  # If the list of books is empty, break out of the loop
        break  # Exit the loop since there are no more pages with books
    
    # Loop through each book found on the page and extract its title and price
    # Extract and print information for each book
    for book in books:  # Loop through each book element found on the page

        # Extract the title of the book
        title = book.h3.a['title']  # The title is located within the <a> tag inside the <h3> tag

        # Extract the price of the book
        price = book.find('p', class_='price_color').text.strip()  
        # This finds the <p> tag with class 'price_color', which contains the price
        # .text gets the text inside the tag, and .strip() removes any extra spaces or newlines

        # Find the rating element within each book
        rating_class = book.find('p', class_='star-rating')['class']  
        # This finds the <p> tag with the class 'star-rating', which contains the rating information
        # ['class'] accesses the list of classes on this tag, which includes a second class (like 'Three') that represents the rating

        # Extract the rating from the second class and convert it to a number
        rating = rating_class[1]  # The second class (e.g., 'Three', 'Four') indicates the star rating in words
        if rating == 'One':
            rating = 1
        elif rating == 'Two':
            rating = 2
        elif rating == 'Three':
            rating = 3
        elif rating == 'Four':
            rating = 4
        elif rating == 'Five':
            rating = 5
        # This if-elif structure converts the rating from words to numbers (e.g., 'Three' becomes 3 stars)

        # Print the book's title, rating, and price in a formatted way
        print(f"Title: {title}\nRating: {rating} stars\nPrice: {price}\n")
        # \n adds a new line after each item, making the output easier to read

    # Go to the next page by incrementing the page counter
    page += 1  # This increases the page number by 1, so the next loop iteration will scrape the next page
