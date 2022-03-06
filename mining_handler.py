import simple_handlers
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver, WebElement


avaible_resources = ['Copper Ore', 'Mysterious Pile Of Rubble',
                     'Common Tree', 'Shrimp', 'Goldfish', 'Coal Ore']


def check_for_ore(driver: WebDriver) -> bool:
    try:
        ore_name = driver.find_element(
            By.XPATH, '//*[@id="travel_data"]/div/div[1]/div[1]/div[4]/div[2]')
        if ore_name.text in avaible_resources:
            return True
        return False
    except NoSuchElementException:
        return False


def mine(driver: WebDriver):
    btn: WebElement
    try:
        btn = driver.find_element(
            By.XPATH, '//*[@id="travel_data"]/div/div[1]/div[1]/div[4]/div[3]/div[2]/button')
        btn.click()
    except NoSuchElementException:
        return
        
    while True:
        sleep(1)
        btn = driver.find_element(By.ID, 'crafting_button')
        if str(btn.text).lower() == 'press here to close':
            break
        btn.click()
