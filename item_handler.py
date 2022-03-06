from matplotlib.style import available
import simple_handlers
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


sellable_raritys = ['uncommon-item', 'common-item', 'rare-item']

sell_locations = {
    'in_fight': {
        'item': '//*[@id="swal2-content"]/div[3]/span',
        'quick_sell': '//*[@id="item-popup"]/div/div/div[2]/div[5]/div[6]/span/a[2]/button',
        'confirm_close': '/html/body/div[3]/div/div[3]/button[1]'
    },
    'walking': {
        'item': '/html/body/div[1]/div[3]/main/div[2]/div[1]/div/div[1]/div[1]/div[4]/div[3]/div/div[2]/span',
        'quick_sell': '//*[@id="item-popup"]/div/div/div[2]/div[5]/div[6]/span/a[2]/button',
        'confirm_close': '/html/body/div[5]/div/div[3]/button[1]'
    }
}


def sell_from(driver: WebDriver, location: str):
    driver.find_element(By.XPATH, sell_locations[location]['item']).click()
    sleep(1.7)
    driver.find_element(
        By.XPATH, sell_locations[location]['quick_sell']).click()
    sleep(1.7)
    driver.find_element(
        By.XPATH, sell_locations[location]['confirm_close']).click()
    sleep(1.7)
    driver.find_element(
        By.XPATH, sell_locations[location]['confirm_close']).click()
    sleep(1.7)


def check_for_selling(driver: WebDriver, location: str) -> bool:
    try:
        element = driver.find_element(
            By.XPATH, sell_locations[location]['item'])

        rarity = element.get_attribute('class')
        if rarity in sellable_raritys:
            return True
        print('You found an item of quality %s' % rarity)
        return False
    except NoSuchElementException:
        return False
