from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(0.5)
driver.get("https://ruderanks-2869.web.app/rude-golems")
time.sleep(10)

rootElement = driver.find_element(By.ID, "scrollDiv")
timeout = 2


def get_window_height(_driver):
    return _driver.execute_script("return window.innerHeight")


def get_next_scroll(start, end):
    return f"scroll({start}, {end})"


currentHeight = get_window_height(driver)

startH = 0
endH = currentHeight

while True:
    

    time.sleep(timeout)
    driver.execute_script(f"document.getElementById('scrollDiv').{get_next_scroll(startH, endH)}")
    startH = endH
    endH += currentHeight




