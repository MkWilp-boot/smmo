import fight_handler
import item_handler
import mining_handler
import captcha_handler
import file_handler
import simple_handlers

from pynput import keyboard

from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

break_program = False

data = {
    'steps_taken': 0,
    'enemys_defeted': 0,
    'itens_sold': 0,
    'resources_taken': 0
}


def stop_app(key):
    global break_program
    global data
    if key == keyboard.Key.end:
        print('end pressed')
        break_program = True
        file_handler.write(data)
        return False


def go_on_walk(driver: WebDriver):
    global data
    exit_from_process = False
    sleep(3)
    walk(driver)

    with keyboard.Listener(on_press=stop_app) as listener:
        while not break_program:
            sleep(2)
            if exit_from_process:
                exit_from_process = False
                walk(driver)
                continue
            if captcha_handler.is_there_captcha(driver):
                exit_from_process = True
                captcha_handler.enter_captcha(driver)
                input('please solve the captcha: ')
                print('Thank you! :)')
            elif fight_handler.check_for_fight(driver):
                exit_from_process = True
                data['enemys_defeted'] += 1
                data = fight_handler.flight(driver)
                simple_handlers.go_to_travel(driver)
            elif mining_handler.check_for_ore(driver):
                exit_from_process = True
                data['resources_taken'] += 1
                mining_handler.mine(driver)
                simple_handlers.go_to_travel(driver)
            elif item_handler.check_for_selling(driver, 'walking'):
                exit_from_process = True
                data['itens_sold'] += 1
                item_handler.sell_from(driver, 'walking')
                simple_handlers.go_to_travel(driver)
            else:
                if can_walk(driver):
                    walk(driver)
    listener.join()
    driver.close()


def can_walk(driver: WebDriver) -> bool:
    if not driver.find_element(By.ID, 'travelBarContainer').is_displayed():
        return True
    return False


def walk(driver: WebDriver):
    global data
    driver.find_element(By.ID, 'primaryStepButton').click()
    data['steps_taken'] += 1
