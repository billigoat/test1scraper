#t1 = tiktok1
import requests
from bs4 import BeautifulSoup

headers = {  # creates a dictionary of HTTP headers
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"  # fakes a browser so Google doesn't block the request
}

res = requests.get("http://www.tiktok.com", headers = headers) #requests from tiktok

soup = BeautifulSoup(res.text, 'html.parser') #start parsing
data = (soup.select('div[data-e2e="video-desc"]'))
print(data)