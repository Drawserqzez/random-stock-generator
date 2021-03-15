import bs4
import random
import requests

URL = 'https://holton.lol/'

print("Hello world!")

page = requests.get(URL)

soup = bs4.BeautifulSoup(page.text, "html.parser")
divs = soup.find_all("div")

for tag in divs:
    print(tag.__str__() + ":D")