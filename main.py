import simple_handlers
import travel_handler
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager


def create_driver():
    s = Service(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=s)
    return driver

def main():
    
    driver = create_driver()
    driver.maximize_window()
    simple_handlers.login(driver)
    simple_handlers.open_close_sidebar(driver)
    simple_handlers.go_to_travel(driver)
    travel_handler.go_on_walk(driver)


if __name__ == '__main__':
    main()
