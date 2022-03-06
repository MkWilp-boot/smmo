from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

credentials = {
    'email': 'joaocwb22@protonmail.com',
    'pwd': 2303022002
}

paths = {
    'base': 'https://web.simple-mmo.com/',
    'login': 'https://web.simple-mmo.com/login',
    'travel': 'https://web.simple-mmo.com/travel'
}


def go_to_travel(driver: WebDriver):
    driver.get(paths['travel'])


def open_close_sidebar(driver: WebDriver):
    btn = driver.find_element(
            By.XPATH, '/html/body/div[1]/div[3]/nav/div/div/div[1]/div[2]/div[1]/button')
    btn.click()


def login(driver: WebDriver):
    driver.get(paths['login'])
    email = driver.find_element(By.ID, 'email')
    pwd = driver.find_element(By.ID, 'password')

    email.clear()
    email.send_keys(credentials['email'])

    pwd.clear()
    pwd.send_keys(credentials['pwd'])

    submit = driver.find_element(
        By.XPATH, '/html/body/div/div[2]/div[1]/form/div[5]/button')
    submit.click()
