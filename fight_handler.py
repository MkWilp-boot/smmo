import item_handler
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def check_for_fight(driver: WebDriver) -> bool:
    try:
        attack_btn = driver.find_element(
            By.XPATH, '//*[@id="travel_data"]/div/div[1]/div[1]/div[4]/div[3]/span[2]/a[1]')
        if attack_btn.text == 'Attack':
            return True
        return False
    except NoSuchElementException:
        return False


def flight(driver: WebDriver, data: dict) -> dict:
    driver.find_element(
        By.XPATH, '//*[@id="travel_data"]/div/div[1]/div[1]/div[4]/div[3]/span[2]/a[1]').click()

    while True:
        sleep(1.5)
        enemy_life = driver.find_element(By.ID, 'opponent-hp')
        if int(enemy_life.text) <= 0:
            break
        driver.find_element(By.ID, 'attackButton').click()

    item_to_sell = item_handler.check_for_selling(driver, location='in_fight')
    if item_to_sell:
        data['itens_sold'] += 1
        item_handler.sell_from(driver, location='in_fight')
    return data
