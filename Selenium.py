from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


website = 'https://www.adamchoi.co.uk/overs/detailed'
path = '/Users/tensaekebede/Downloads/chromedriver-mac-arm64/chromdrive'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options) #Driver Attribute
driver.get(website)

# Finding Elements
all_matches_button = driver.find_element(by="xpath",value='//label[@analytics-event="All matches"]') #'//label[@analytics-event="All matches"]'
all_matches_button.click()

matches = driver.find_elements(By.TAG_NAME, 'tr')
matches = WebDriverWait(driver, 100).until(EC.presence_of_all_elements_located((By.TAG_NAME, 'tr')))
date = []
home_team = []
score = []
away_team = []

for match in matches:
    print(match.text)


time.sleep(10) 
#driver.quit()