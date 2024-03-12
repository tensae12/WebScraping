from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options #Instead of displaying the browser window, the browser operates in the background
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

###################------Scraping a single page with Selenium---------###############
options = Options()
options.add_argument('--headless')  #Instead of displaying the browser window, the browser operates in the background


web = 'https://www.audible.com/search'
path = '/Users/tensaekebede/Downloads/chromedriver-mac-arm64/chromdrive'
chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=chrome_options)
driver.get(web)
driver.maximize_window()
container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
products = container.find_elements(By.XPATH, './li')
products = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "productListItem")]')))



book_title = []
book_author = []
book_length = []


for product in products:

    book_title.append(product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

driver.quit()



df = pd.DataFrame({'Book Title': book_title, 'Author': book_author, 'Runtime': book_length})
df.to_csv('books.csv', index=False)

