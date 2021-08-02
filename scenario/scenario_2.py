import logging
from seleniumDriver.driver import Driver
from time import sleep
from timeit import default_timer as timer
from datetime import timedelta
from portal.login.login import Login
from portal.selectMenu.dataRegistration import Data_registration
from selenium import common


class Scenario_2:
    def __init__(self, scenario_url=None):
        self.scenario_url = scenario_url

    def start(self):
        logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='log/scenario_1.log', level='INFO')
        try:
            logging.info('start')
            start_time = timer()
            print("\033[32m" + "Process start" + "\033[0m")
            driver = Driver()
            driver.get_url(self.scenario_url)

            logging.info('Loing start, ID:lwjtest3')
            portal_login = Login('lwjtest3', 'welcome1!', driver)
            portal_login.alert_page_check()
            portal_login.portal_login_page_in()
            portal_login.portal_login()
            portal_login.alert_check_accept()
            sleep(1)

            data_registration = Data_registration(driver)
            data_registration.select_data_registration()
            sleep(1)

            driver.close()
            driver.quit()
            end_time = timer()
            logging.info('Process end')
            print('\033[32m' + 'Process end' + '\033[0m')
            print('Total run time: ' + '\033[35m' + str(timedelta(seconds=end_time - start_time)) + '\033[0m')
        except common.exceptions.WebDriverException:
            print('\033[31m' + '**selenium webDriver error**' + '\033[0m')
            sleep(5)
            driver.close()
            driver.quit()
            logging.info('error end')
        except AttributeError as e:
            print('\033[31m' + '**AttributeError**' + '\033[0m')
            print('\033[31m' + '**Message : ' + str(e) + '**' + '\033[0m')
            sleep(5)
            driver.close()
            driver.quit()
            logging.info('error end')
        except TypeError as e:
            print("\033[31m" + "**TypeError**" + "\033[0m")
            print("\033[31m" + "**Message : " + str(e) + "**" + "\033[0m")
            sleep(5)
            driver.close()
            driver.quit()
            logging.info('error end')
