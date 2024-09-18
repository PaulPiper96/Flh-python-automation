
import requests
from bs4 import BeautifulSoup
import re

# URL of the Wikipedia article
url = "https://de.wikipedia.org/wiki/Ozonabbau"

# Send a request to fetch the page content
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <p> tags (paragraphs)
paragraph_tags = soup.find_all('p')

# Iterate through each <p> tag
for paragraph in paragraph_tags:
    # Extract the text from the paragraph tag
    paragraph_text = paragraph.get_text()

    # Print the full paragraph text
   


    # Search for the word "Uv" (case-insensitive) in the paragraph text
    matches = re.findall(r'\bUv\b', paragraph_text, flags=re.IGNORECASE)

    # Print each match found
    for match in matches:
        print(f"Found '{match}'")
        print(paragraph_text)
        print("-------------")