from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import openpyxl
from openpyxl import Workbook

# Set up a Selenium WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to The Defiant website
url = "https://thedefiant.io/news/defi"
driver.get(url)

# Wait for the page to load (optional)
time.sleep(3)  # Adjust the sleep time according to your needs

# Find and extract recent article names
recent_articles = driver.find_elements(By.XPATH, "//a/h3")

topics_list = [] # Use later to put in list (with .append)
for link in recent_articles:
    topics_list.append(link.text)
    print(topics_list)

# Find and extract all links on DeFi page

links = driver.find_elements(By.TAG_NAME, 'a')

links_list = []
for link in links:
   # get_attribute() to get all href
   attr_links = link.get_attribute("href")
   links_list.append(attr_links)
   print(links_list)

# Create empty excel
workbook = Workbook()
workbook.save(filename="sample.xlsx")

# Write topics_list and links_list to Excel columns
d = [topics_list, links_list]
df = pd.DataFrame(data=d)
excel_file = "sample.xlsx"
df.to_excel(excel_file, index=False)

# for index, val in enumerate(links):
#     print(index, val)
#     links = driver.find_elements(By.XPATH, '//a/h3 [href]')
#     ActionChains(driver)\
#         .click(links[0]).perform()

# Close the WebDriver instance
driver.quit()

