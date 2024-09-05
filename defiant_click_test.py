from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
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

# Wait for the page to load 
time.sleep(3) 

# Get list of article links
links_list = [article.get_attribute("href") for article in driver.find_elements(By.XPATH, "//section[@class=mt-4]/div[1]>a")]

#? Full XPath: /html/body/div[1]/main/section/div[1]>a
#? XPath: /html/body/div[1]/main/section/div[1]/div[1]/div[2]/a
# Filter list a bit for whichever contain 'news'
filtered_list = [list for list in links_list if 'news' in list]
# Filter again for duplicates
unduplicated_list = list(set(filtered_list))
print(unduplicated_list)

# Open each item in a new browser tab?
#TODO: Click on each 'href' (I think), click on author name, scrape articles from author

for list_item in unduplicated_list:
    driver.get((list_item)) # Open tabs for each link
    author = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/article/div[2]/a').click()
    print(author)
    


#TODO: Click on Page 2 Button, repeat actions above
#TODO: driver.switchTo().alert().dismiss(); for popups (this is javascript I think but maybe okay)

#TODO: Change to openpyxl format
d = [unduplicated_list]
df = pd.DataFrame(data=d)
excel_file = "sample.xlsx"
df.to_excel(excel_file, index=False)




# for link in recent_articles:
#     links = driver.find_elements(By.XPATH, '//a/h3 [href]') #! Fix this according to recent_articles XPATH
#     ActionChains(driver)\
#         .click(links[0]).perform()

# Find and extract all links on DeFi page

# links = driver.find_elements(By.TAG_NAME, 'a')

# links_list = []
# for link in links:
#    # get_attribute() to get all href
#    attr_links = link.get_attribute("href")
#    links_list.append(attr_links)
#    print(links_list)

# Create empty excel
# workbook = Workbook()
# workbook.save(filename="sample.xlsx")

# Write topics_list and links_list to Excel columns
# d = [topics_list, links_list]
# df = pd.DataFrame(data=d)
# excel_file = "sample.xlsx"
# df.to_excel(excel_file, index=False)

# for index, val in enumerate(links):
#     print(index, val)
#     links = driver.find_elements(By.XPATH, '//a/h3 [href]')
#     ActionChains(driver)\
#         .click(links[0]).perform()

# Close the WebDriver instance
driver.quit()

