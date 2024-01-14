import csv

from bs4 import BeautifulSoup as BS
from selenium import webdriver
from functools import reduce
import pandas as pd
import time

page = 'https://www.datacentermap.com/usa/'

def render_page(url):
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    r = driver.page_source
    driver.quit()
    return r


def scraper(page, states):
    output = pd.DataFrame()
    datacenter_list = []
    for s in states:
        url = str(page) + s
        print(url)
        r = render_page(url)

        soup = BS(r, "html.parser")
        table = soup.findAll("table")[0]

        for el in soup.findAll('tr'):
            data = el.findAll('td')
            if not data:
                continue
            city_name = data[0].findAll('a')[0].text
            number = data[1].text

            one_problem = [s, city_name, number]
            datacenter_list.append(one_problem)

    print(datacenter_list)
    with open('us-states-datacenters.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(datacenter_list)


state_names = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Guam", "Hawaii", "Iowa", "Idaho",
               "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine",
               "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota",
               "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma",
               "Oregon", "Pennsylvania", "Puerto Rico", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
               "Texas", "Utah", "Virginia", "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia",
               "Wyoming"]

scraper(page, state_names)
