from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver') # Downloaad the chrome driver and replace this path
driver.get("https://quotes.toscrape.com/") # Wait for some element to be rendered or just a blind sleep
print(driver.page_source) # This'll give you the full rendered HTML

driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
time.sleep(10)

soup = BeautifulSoup(driver.page_source, 'html.parser')
golem = soup.find('main')
print(golem)
print(driver)
driver.close()