import requests
import sys
from bs4 import BeautifulSoup

result = requests.get(sys.argv[1])

soup = BeautifulSoup(result.text, 'html.parser')

h1_tags = soup.find_all('h1')

for tag in h1_tags:
    print(tag.get_text())

print(sys.argv)