#n1 = nike1
import requests
from bs4 import BeautifulSoup

headers = {  # creates a dictionary of HTTP headers
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  # fakes a browser so Google doesn't block the request
}

res = requests.get("https://www.nike.com/w/mens-shoes-nik1zy7ok", headers=headers)
print(res.status_code)  # prints the HTTP status code (e.g. 200 means OK)

soup = BeautifulSoup(res.text, 'html.parser') #starts parsing
data = (soup.select('a.product-card__link-overlay'))#selects specific data
print(data)
for x in data:
    print(x.text)


#<a class="product-card__link-overlay" data-testid="product-card__link-overlay" href="https://www.nike.com/t/air-jordan-3-retro-pure-money-mens-shoes-5M3ZlK/CT8532-111" tabindex="-1">Air Jordan 3 Retro "Pure Money"</a>