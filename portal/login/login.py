from seleniumDriver import driver
from util.randomTyping import random_typing
import logging


class Login:
    def __init__(self, login_id=None, login_pw=None, get_driver=None):
        self._id = login_id
        self._pw = login_pw
        self._driver = get_driver
        logging.info(f"Login ID: {self._id}, Login PW: {self._pw}")
        print(f"Login ID: {self._id}, Login PW: {self._pw}")

    def alert_page_check(self):
        print("\033[32m" + "alert page check" + "\033[0m")
        title_text = self._driver.get_title(10)
        if title_text == '개인정보 보호 오류':
            self._driver.find_by_id('details-button', 10).click()
            self._driver.find_by_id('proceed-link', 10).click()
        else:
            print("alert page not found")

    def portal_login_page_in(self):
        print("\033[32m" + "into the login page" + "\033[0m")
        driver.Driver.find_by_class(self._driver, 'mypage', 10).click()


    def portal_login(self):
        print("\033[32m" + "portal login" + "\033[0m")
        select_name_box = driver.Driver.find_by_id(self._driver, 'loginId', 10)
        random_typing(select_name_box, self._id, 0.00, 0.20)
        select_pw_box = driver.Driver.find_by_id(self._driver, 'loginPw', 10)
        random_typing(select_pw_box, self._pw, 0.00, 0.20)
        driver.key_in_enter(select_pw_box)

    def alert_check_accept(self):
        try:
            driver.Driver.find_alert(self._driver, 10)
        except:
            print('alert_check error')
        else:
            alert = driver.Driver.switch_alert(self._driver)
            print('alert message: "' + alert.text + '"')
            alert.accept()