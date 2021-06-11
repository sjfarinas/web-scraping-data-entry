from selenium import webdriver
from dotenv import dotenv_values
import time

config = dotenv_values(".env")
GOOGLE = config.get("GOOGLE_FORM")
CHROME_DRIVER_PATH = config.get("CHROME_DRIVER_PATH")


class GoogleForm:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def fill_form(self, addresses=[], prices=[], links=[]):
        self.driver.get(GOOGLE)
        for i in range(len(addresses)):
            address = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/div/div/input')
            time.sleep(1)
            address.send_keys(addresses[i])

            price = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div/div/input')
            time.sleep(1)
            price.send_keys(prices[i])

            link = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div/div/input')
            time.sleep(1)
            link.send_keys(links[i])

            submit_button = self.driver.find_element_by_xpath('/html/body/div/div[2]/form/div[2]/div/div[3]/div/div/div')
            time.sleep(1)
            submit_button.click()

            another = self.driver.find_element_by_xpath('/html/body/div/div/div/div/div[4]/a')
            time.sleep(1)
            another.click()

        self.driver.quit()
