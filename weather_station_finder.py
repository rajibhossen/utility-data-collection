from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def get_station_keyword(state, city_name):
    driver.get("https://www.wunderground.com/history/daily/us/" + state + "/" + city_name)

    driver.find_element(By.XPATH, "/html/body/app-root/app-history/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div[2]/section/div[2]/div[1]/div[1]/div[1]/div/lib-date-selector/div/input").click()
    print(driver.current_url)

print(get_station_keyword("tx", "dallas"))