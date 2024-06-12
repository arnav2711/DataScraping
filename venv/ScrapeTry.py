import requests
from bs4 import BeautifulSoup

req = requests.get("https://hbits.co/")

soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify())
