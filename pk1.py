import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
#pk1 = pokemon1
service = Service(r'C:\Users\etern\OneDrive\Desktop\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://serebii.net/pokedex-sv/bug.shtml')
print("Press the ` key (above tab) to close browser")

page_source = BeautifulSoup(driver.page_source, 'html.parser') #taking page source and making it a BS4 object
pt = page_source.select('table[class="dextable"] tbody tr')

print (pt[50])

keyboard.wait('`')
driver.quit()
print("Browser closed.")