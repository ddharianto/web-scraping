import csv
import requests
from bs4 import BeautifulSoup

# send a GET request to the website
url = 'https://www.bbc.com/news/world-europe-64986486'
response = requests.get(url)

# parse the HTML content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# find all anchor tags that contain a URL
urls = [link.get('href') for link in soup.find_all('a') if link.get('href')]

# write the URLs to a CSV file
with open('urls.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for url in urls:
        writer.writerow([url])