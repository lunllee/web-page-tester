from seleniumDriver.driver import Driver
from time import sleep
from timeit import default_timer as timer
from datetime import timedelta
from admin.login.login import Login
from admin.selectMenu.dataManager import Data_manager
from selenium import common


class Scenario:
    def __init__(self, scenario_url=None):
        self.scenario_url = scenario_url

    def start(self):
        try:
            start_time = timer()
            print("\033[32m" + "Process start" + "\033[0m")
            driver = Driver()
            driver.get_url(self.scenario_url)

            admin_login = Login('lwjtest3', 'welcome1!', driver)
            admin_login.alert_page_check()
            admin_login.admin_login()
            admin_login.alert_check_accept()
            sleep(1)

            data_manager = Data_manager(driver)
            data_manager.select_dataset_manager_list()
            data_manager.select_dataset_list()
            dataset_result = data_manager.dataset_save_process()
            print("Save dataset title : " + "\033[32m" + dataset_result + "\033[0m")
            sleep(1)

            driver.close()
            driver.quit()
            end_time = timer()
            print("\033[32m" + "Process end" + "\033[0m")
            print("Total run time: " + "\033[35m" + str(timedelta(seconds=end_time - start_time)) + "\033[0m")
        except common.exceptions.WebDriverException:
            print("\033[31m" + "**selenium webDriver error**" + "\033[0m")
            sleep(5)
            driver.close()
            driver.quit()
        except AttributeError as e:
            print("\033[31m" + "**AttributeError**" + "\033[0m")
            print("\033[31m" + "**Message : " + str(e) + "**" + "\033[0m")
            sleep(5)
            driver.close()
            driver.quit()
        except TypeError as e:
            print("\033[31m" + "**TypeError**" + "\033[0m")
            print("\033[31m" + "**Message : " + str(e) + "**" + "\033[0m")
            sleep(5)
            driver.close()
            driver.quit()
