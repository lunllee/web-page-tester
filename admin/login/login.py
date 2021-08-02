from seleniumDriver import driver
from util.randomTyping import random_typing


class Login:
    def __init__(self, login_id=None, login_pw=None, get_driver=None):
        self.login_id = login_id
        self.login_pw = login_pw
        self.get_driver = get_driver
        print(f"Login ID: {self.login_id}, Login PW: {self.login_pw}")

    def alert_page_check(self):
        print("\033[32m" + "alert page check" + "\033[0m")
        title_text = self.get_driver.get_title(10)
        if title_text == '개인정보 보호 오류':
            self.get_driver.find_by_id('details-button', 10).click()
            self.get_driver.find_by_id('proceed-link', 10).click()
        else:
            print("alert page not found")

    def admin_login(self):
        print("\033[32m" + "admin login" + "\033[0m")
        select_name_box = driver.Driver.find_by_id(self.get_driver, 'loginId', 10)
        random_typing(select_name_box, self.login_id, 0.00, 0.20)
        select_pw_box = driver.Driver.find_by_id(self.get_driver, 'loginPw', 10)
        random_typing(select_pw_box, self.login_pw, 0.00, 0.20)
        driver.key_in_enter(select_pw_box)

    def alert_check_accept(self):
        try:
            driver.Driver.find_alert(self.get_driver, 10)
        except:
            print('alert_check error')
        else:
            alert = driver.Driver.switch_alert(self.get_driver)
            print('alert message: "' + alert.text + '"')
            alert.accept()
