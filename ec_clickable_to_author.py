from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
import openpyxl
from openpyxl import Workbook

# Set up a Selenium WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to The Defiant website
url = "https://thedefiant.io/news/DeFi"
driver.get(url)

# Wait for the page to load 
time.sleep(1) 

#TODO: Click on each 'href' (I think), click on author name, scrape articles from author

actions = ActionChains(driver)

# Get list of Recent Articles as web elements
links_list = [link for link in driver.find_elements(By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a")]
# print(links_list)

# Get list of Recent Articles as links
clickable_links = []
for link in links_list:
    attr_link = link.get_attribute("href")
    clickable_links.append(attr_link)
    # print(clickable_links)

#TODO: Everything working, except for XPATH to author
#TODO: Create for loop to do for each index
#! TO FIX: Now that we have a list of clickable Recent Article links, need to load them, target author, click author. Can do on their own I guess?

# Get author info
nav_to_article = driver.get(clickable_links[0]) # Navigate to first DeFi Recent Articles link
author_attribute = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//article/div[2]/a[@href]"))).get_attribute("href")
print(author_attribute)
author_link = driver.find_element(By.XPATH, "//article/div[2]/a[@href]").click()
time.sleep(5)
#! Not throwing any errors, but not clicking to author page :/

# Click on author link
author_link = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//article/div[2]/a[@href]")))
print(author_link.text) # Author's name
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//main/div[2]/div/div[1]/div/a")))  # Wait for page to load #TODO: Maybe chance this
# /html/body/div[1]/main/div/div[2]/article/div[2]/a
author_articles = [article for article in driver.find_elements(By.XPATH, "//main/div[2]/div/div[1]/div/a")] # Get list of author's articles as web elements

# Get list of Recent Articles as links
clickable_articles = []
for article in author_articles:
    attr_link = article.get_attribute("href")
    clickable_links.append(attr_link)
    print(clickable_articles)




# for index, val in enumerate(clickable_links):
#     #get the links again after getting back to the initial page in the loop
#     #! BELOW: Need to regenerate the links in the same way as above? Or how to get and click the HREF links one by one (not as web elements). Check [@href] section
#     links_list = driver.find_elements(By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a")
#     #scroll to the n-th link, it may be out of the initially visible area
#     actions.move_to_element(links_list[index]).perform()
#     links_list[index].click()
#     driver.get(val)
#     #scrape the data on the new page and get back with the following command
#     author = driver.find_element(By.XPATH, "//div[contains(@class,'mb-4')]//a[@href]")
#     print(author)
#     driver.execute_script("window.history.go(-1)") #you can alternatevely use this as well: driver.back()
#     WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a[@href]")))
#     time.sleep(2)
