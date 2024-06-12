import requests
from bs4 import BeautifulSoup

req = requests.get("https://en.wikipedia.org/wiki/Bharatiya_Janata_Party")

soup = BeautifulSoup(req.content, "html.parser")

r = soup.find_all("body", class_ = "")

print(r)
