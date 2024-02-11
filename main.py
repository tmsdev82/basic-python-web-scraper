import requests
import sys

result = requests.get(sys.argv[1])

print(result.text)
print(sys.argv)