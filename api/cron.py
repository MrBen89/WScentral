import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from .models import Game

def printgames():
    games = Game.object.all()
    print(games)



url = "https://jp.mercari.com/search?keyword=グンペイ%E3%80%80ワンダースワン"
response = requests.get(url)
html_content = response.text

browser = webdriver.Chrome()
# browser = webdriver.Chrome()
browser.get(url)


time.sleep(2)

prices = browser.find_elements(By.CSS_SELECTOR, "[class*='number']")
prices_num = []

for price in prices:
        prices_num.append(int(price.text.replace(",", "")))

average_price = sum(prices_num)/len(prices_num)

print(average_price)

def scrape():
        # Your task logic here
        print("This job runs every 5 minutes!")

