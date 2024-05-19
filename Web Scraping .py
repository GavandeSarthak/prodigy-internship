import csv
import requests
from bs4 import BeautifulSoup

def scrape_amazon_bestsellers(category_url):
    # Send a GET request to the category URL
    response = requests.get(category_url)
    if response.status_code != 200:
        print("Failed to retrieve data from Amazon.")
        return

    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the product containers
    product_containers = soup.find_all('div', class_='a-section a-spacing-medium')

    # Open a CSV file to store the data
    with open('amazon_bestsellers.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Extract product information and write to CSV
        for container in product_containers:
            name = container.find('span', class_='a-text-normal').text.strip()
            price = container.find('span', class_='a-price').text.strip()
            rating = container.find('span', class_='a-icon-alt').text.strip()
            writer.writerow({'Name': name, 'Price': price, 'Rating': rating})

    print("Scraping completed. Data saved to amazon_bestsellers.csv")

# URL of the Best Sellers page in a specific category on Amazon
category_url = "https://www.amazon.com/Best-Sellers-Electronics/zgbs/electronics/"
scrape_amazon_bestsellers(category_url)
