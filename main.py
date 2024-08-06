import requests
import sys
from bs4 import BeautifulSoup

result = requests.get(sys.argv[1])

soup = BeautifulSoup(result.text, 'html.parser')

h1_tags = soup.find_all('h1')

for tag in h1_tags:
    print(tag.get_text())
    
ul_list = soup.find_all('ul')

print(f"number of items: {len(ul_list)}")

for index, ul_element in enumerate(ul_list):
    print(f"{index}: {ul_element.get_text()}")
    print("-----")
    
parent_div = soup.find('div', {'data-testid': 'quote-statistics'})
stats_ul = parent_div.find('ul')

list_items = stats_ul.find_all('li')
for item in list_items:
    columns = item.find_all('span')    
    print(f"{columns[0].get_text()}: {columns[1].get_text()}")

print(sys.argv)