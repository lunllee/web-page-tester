from selenium import webdriver
from selenium import common
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import chromedriver_autoinstaller


def find_all_by_tag_with_obj(get_obj, get_tag, get_time):
    return WebDriverWait(get_obj, get_time).until(
        ec.presence_of_all_elements_located(
            (By.TAG_NAME, get_tag)))


def key_in_enter(get_obj):
    get_obj.send_keys(Keys.RETURN)


class Driver:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument("window-size=1920x1080")
        get_chrome_var = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
        try:
            self.driver = webdriver.Chrome(executable_path=f"{get_chrome_var}/chromedriver.exe", options=options)
        except common.exceptions.WebDriverException:
            chromedriver_autoinstaller.install(True)
            self.driver = webdriver.Chrome(executable_path=f"{get_chrome_var}/chromedriver.exe", options=options)
        except FileNotFoundError:
            chromedriver_autoinstaller.install(True)
            self.driver = webdriver.Chrome(executable_path=f"{get_chrome_var}/chromedriver.exe", options=options)

    def __call__(self):
        return self.driver

    def get_url(self, url: str):
        self.driver.get(url)
        print(f"conn URL: {url}")

    def get_stay_url(self):
        print(f"stay URL: {self.driver.current_url}")
        return self.driver.current_url

    def get_title(self, get_time):
        WebDriverWait(self.driver, get_time).until(
            ec.presence_of_element_located(
                (By.TAG_NAME, 'title')))
        print(f"get title: {self.driver.title}")
        return self.driver.title

    def find_by_id(self, get_id, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_element_located(
                (By.ID, get_id)))
        return result

    def find_by_name(self, get_name, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_element_located(
                (By.NAME, get_name)))
        return result

    def find_by_class(self, get_class, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_element_located(
                (By.CLASS_NAME, get_class)))
        return result

    def find_by_tag(self, get_tag, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_element_located(
                (By.TAG_NAME, get_tag)))
        return result

    def find_by_xpath(self, get_xpath, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_element_located(
                (By.XPATH, get_xpath)))
        return result

    def find_all_by_name(self, get_name, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_all_elements_located(
                (By.NAME, get_name)))
        return result

    def find_all_by_class(self, get_class, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_all_elements_located(
                (By.CLASS_NAME, get_class)))
        return result

    def find_all_by_tag(self, get_tag, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_all_elements_located(
                (By.TAG_NAME, get_tag)))
        return result

    def find_by_link(self, get_text, get_time):
        result = WebDriverWait(self.driver, get_time).until(
            ec.presence_of_all_elements_located(
                (By.LINK_TEXT, get_text)))
        return result

    def find_alert(self, get_time):
        return WebDriverWait(self.driver, get_time).until(ec.alert_is_present())

    def switch_alert(self):
        return self.driver.switch_to_alert()

    def close(self):
        self.driver.close()
        print(f"selenium driver close")

    def quit(self):
        self.driver.quit()
        print(f"selenium driver quit")
