import time
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import csv


driver = webdriver.Chrome('./chromedriver')

options = Options()
options.add_argument('--headless')

url = "https://ruderanks-2869.web.app/rude-golems"
initialTimeSleep = 20

driver.implicitly_wait(0.5)
driver.get(url)


def get_window_height(_driver):
    return _driver.execute_script("return window.innerHeight")


def get_next_scroll(start, end):
    return f"scroll({start}, {end})"


def is_scroll_on_bottom(_driver):
    return _driver.execute_script("return (window.innerHeight + window.scrollY) >= document.body.offsetHeigh")


rootElement = None

while not rootElement:
    try:
        rootElement = driver.find_element(By.ID, "scrollDiv")
    except NoSuchElementException:
        print("Error getting scrollDiv")
        pass


currentHeight = get_window_height(driver)
startH = 0
endH = currentHeight

ranks = []
ids = []

while not is_scroll_on_bottom(driver):
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    golem_cards = soup.find_all('div', class_='styles_card__7uWFB')

    for golem_card in golem_cards:
        golem_id = golem_card.find('div', class_='styles_name__XaPxb').text
        if golem_id not in ids:
            ids.append(golem_id)
    driver.execute_script(f"document.getElementById('scrollDiv').{get_next_scroll(startH, endH)}")
    startH = endH
    endH += currentHeight

    file = open('lib/data.csv', 'w+', newline='')
    with file:
        write = csv.writer(file)
        write.writerow(ids)


