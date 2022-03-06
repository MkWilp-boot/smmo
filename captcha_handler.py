from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


def enter_captcha(driver: WebDriver):
    driver.find_element(
        By.XPATH, '//*[@id="travel_data"]/div/div[1]/div[1]/div[4]/div[3]/div/a').click()


def is_there_captcha(driver: WebDriver) -> bool:
    try:
        btn = driver.find_element(
            By.XPATH, '//*[@id="travel_data"]/div/div[1]/div[1]/div[4]/div[3]/div/a')
        if str(btn.text).lower().__contains__('verify'):
            return True
        return False
    except NoSuchElementException:
        return False
