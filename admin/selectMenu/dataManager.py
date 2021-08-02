import pandas as pd
from time import sleep
from seleniumDriver import driver
from util.randomTyping import random_typing
from selenium.webdriver.support.ui import Select


class Data_manager:
    def __init__(self, get_driver=None):
        self.get_driver = get_driver

    def alert_check_accept(self):
        try:
            alert = driver.Driver.find_alert(self.get_driver, 10)
        except:
            print('alert_check error')
        else:
            alert_message = alert.text
            print('alert message: "' + alert_message + '"')
            alert.accept()
            return alert_message

    def select_dataset_manager_list(self):
        print("\033[32m" + "select dataset menager list" + "\033[0m")
        driver.Driver.find_by_xpath(self.get_driver, "//*/span[text()='데이터관리']", 10).click()

    def select_dataset_list(self):
        print("\033[32m" + "select dataset list" + "\033[0m")
        driver.Driver.find_by_xpath(self.get_driver, "//div[@id='data']/div/a[text()='데이터관리']", 10).click()

    def dataset_save_process(self):
        print("\033[32m" + "dataset save process start" + "\033[0m")
        driver.Driver.find_by_xpath(self.get_driver, "//a[text()='등록']", 10).click()

        sc = pd.read_excel('C:/Users/lwj07/PycharmProjects/webTestProject/xlsx/admin_dataset_save_select_category.xlsx',
                           sheet_name='Sheet1')

        for lab, row in sc.iterrows():
            print('\033[31m' + 'key id' + '\033[0m' + ' = "' + str(row['id']) + '"')
            print('\033[31m' + 'value' + '\033[0m' + ' = "' + str(row['value']) + '"')
            if 'categoryLv4Select' == row['id']:
                if pd.isnull(row['value']):
                    driver.Driver.find_by_id(self.get_driver, 'categoryAddBtn', 5).click()
                    continue
            elif pd.isnull(row['value']):
                continue

            select_dropdown_box = Select(driver.Driver.find_by_id(self.get_driver, row['id'], 10))
            select_dropdown_box.select_by_visible_text(row['value'])
            sleep(1)
            if 'categoryLv4Select' == row['id']:
                driver.Driver.find_by_id(self.get_driver, 'categoryAddBtn', 5).click()

        f = pd.read_excel('C:/Users/lwj07/PycharmProjects/webTestProject/xlsx/admin_dataset_save.xlsx',
                          sheet_name='Sheet1')

        dataset_title = ''
        for lab, row in f.iterrows():
            print('\033[31m' + 'key id' + '\033[0m' + ' = "' + str(row['id']) + '"')
            print('\033[31m' + 'value' + '\033[0m' + ' = "' + str(row['value']) + '"')
            if 'titleText' == row['id']:
                dataset_title = row['value']

            if pd.isnull(row['value']):
                continue

            select_box = driver.Driver.find_by_id(self.get_driver, row['id'], 10)
            if select_box.get_attribute('type') == 'date':
                select_box.send_keys(row['value'])
            else:
                random_typing(select_box, str(row['value']), 0.00, 0.05)

        driver.Driver.find_by_xpath(self.get_driver, "//a[text()='저장']", 10).click()
        check_alert = self.alert_check_accept()
        if check_alert != "데이터 셋이 등록되었습니다.":
            print('\033[31m' + '**data save error**' + '\033[0m')
            print('\033[31m' + '**message : ' + check_alert + '**' + '\033[0m')
        print("\033[32m" + "dataset save process end" + "\033[0m")
        driver.Driver.get_stay_url(self.get_driver)
        sleep(3)
        return dataset_title

