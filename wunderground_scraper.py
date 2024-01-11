from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
import pandas as pd
import time


def render_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r


def scraper(page, locations, dates):
    output = pd.DataFrame()

    for l in locations:

        for d in dates:

            url = str(str(page) + l + "/date/" + str(d))
            print(url)
            r = render_page(url)

            soup = BS(r, "html.parser")
            container = soup.find('lib-city-history-observation')
            check = container.find('tbody')

            daily_data = []
            data = []

            for c in check.find_all('tr', class_='ng-star-inserted'):
                for i in c.find_all('td', class_='ng-star-inserted'):
                    trial = i.text
                    trial = trial.strip('  ')
                    data.append(trial)

            print(data)
            print(len(data))
            for i in range(0, len(data), 10):
                hourly_data = data[i:i + 10]
                daily_data.append(hourly_data)
            print(daily_data)
    print('Scraper done!')

    return output


dates = ['2024-1-5']
locations = ["KSJC", "KDFW"]
page = 'https://www.wunderground.com/history/daily/'
df_output = scraper(page, locations, dates)
