import keyboard
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service(r'C:\Users\etern\OneDrive\Desktop\chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.random.org/integers/')
num_numbers = driver.find_element(By.CSS_SELECTOR, 'input[name="num"]') #finds the button for # of integers
num_numbers.clear() #clears the numbers button
num_numbers.send_keys('5') #puts 5
get_numbers = driver.find_element(By.CSS_SELECTOR, 'input[value="Get Numbers"]')
get_numbers.click()

keyboard.wait('`')
driver.quit()
