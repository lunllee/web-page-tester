import pandas as pd
from time import sleep
from seleniumDriver import driver
from util.randomTyping import random_typing
from selenium.webdriver.support.ui import Select


class Data_registration:
    def __init__(self, get_driver=None):
        self._driver = get_driver

    def select_data_registration(self):
        print("\033[32m" + "select data registration" + "\033[0m")
        driver.Driver.find_by_xpath(self._driver, "//a[@href ='/dataset/write.web']", 10).click()
