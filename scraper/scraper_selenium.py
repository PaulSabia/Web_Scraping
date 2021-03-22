from time import sleep
from datetime import datetime
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import unquote
import re
from conn import Connecteur

# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

url = "https://www.boursedirect.fr/fr/actualites"

class Scraper:
    def __init__(self, url, reset=False):
        self.url = unquote(url)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)
        # self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.get(url)
        sleep(random.randrange(1,5))

        self.reset = reset
        self.scraping()


    def scraping(self, scraping=True, time_start=datetime.now()):
        if self.reset == True:
            Connecteur.reset_database()

        while scraping:
            points = self.driver.find_element_by_xpath('//*[@id="graph-tab"]/div/div/span[2]/span[1]').text
            points = re.sub('[^0-9. \n]', '', points)
            pourcent = self.driver.find_element_by_xpath('//*[@id="graph-tab"]/div/div/span[3]').text
            pourcent = pourcent.replace('+','').replace('%', '').replace(' ','')

            Connecteur.insert_data(points, pourcent)

            time_end = datetime.now()
            if time_end.hour-time_start.hour == 24:
                scraping=False

            sleep(30)

if __name__ == '__main__':
    go_scraping = Scraper(url)




