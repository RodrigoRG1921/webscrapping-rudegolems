from selenium import webdriver
import time
from lxml import html
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

options = Options()
options.add_argument('--headless')


driver = webdriver.Chrome('./chromedriver')
driver.get("https://ruderanks-2869.web.app/rude-golems")
# page_source stores the HTML markup of the webpage, not the JavaScript code.

driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
time.sleep(10)
element = driver.find_element(By.ID, 'scrollDiv')

SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = driver.execute_script("return document.documentElement.scrollHeight")
print(f"last height ${last_height}")

while True:
    # Scroll down to bottom

    # content = driver.find_element(By.CLASS_NAME, 'content')
    print(element)
    print("eto")

    driver.execute_script("arguments[0].scrollIntoView(true);", element);
    size = element.size
    w, h = size['width'], size['height']
    print(f"element height: {h}")

    touch_action = webdriver.TouchActions(driver)
    touch_action.scroll_from_element(recent_list[1], 0, 150).perform()

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    golems = soup.find_all('div', class_='styles_name__XaPxb')

    for golem in golems:
        print(golem.text)

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height






