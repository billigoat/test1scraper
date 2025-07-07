# scraper-python.py
# To run this script, paste `python scraper-python.py` in the terminal

import requests # make a web call
from bs4 import BeautifulSoup #self explanatory


def scrape(): #defines a function called scrape
    url = 'https://www.example.com' #target
    response = requests.get(url) #asks website for its data
    soup = BeautifulSoup(response.text, 'html.parser') #parses HTML data
    title = soup.select_one('h1').text
    text = soup.select_one('p').text
    link = soup.select_one('a').get('href')

    print(title)
    print(text)






if __name__ == '__main__': #checks if this script is being run
    scrape() #runs script (only if true) (stops from running automatically)
