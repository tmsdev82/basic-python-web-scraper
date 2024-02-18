import requests
import sys
from bs4 import BeautifulSoup

result = requests.get(sys.argv[1])

soup = BeautifulSoup(result.text, 'html.parser')

h1_tags = soup.find_all('h1')

for tag in h1_tags:
    print(tag.get_text())
    
tables = soup.find_all('table')

print(f"number of tables: {len(tables)}")

for index, table in enumerate(tables):
    print(f"{index}: {table.get_text()}")
    print("-----")
    
div = soup.find('div', {'data-test': 'left-summary-table'})
table = div.find('table')
print(f"left table: {table.get_text()}")

div = soup.find('div', {'data-test': 'right-summary-table'})
table = div.find('table')
print(f"right table: {table.get_text()}")


print(sys.argv)