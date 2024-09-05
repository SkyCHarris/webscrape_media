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
url = "https://thedefiant.io/news/DeFi"
driver.get(url)

# Wait for the page to load 
time.sleep(1) 

#TODO: Click on each 'href' (I think), click on author name, scrape articles from author

actions = ActionChains(driver)

links_list = [link for link in driver.find_elements(By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a")]
new_links_list = []
for link in links_list:
   # get_attribute() to get all href
   attr_links = link.get_attribute("href")
   links_list.append(attr_links)
   print(links_list)
# print(links_list)
#TODO: Fix stale element for link.click() (Likely need to move to new web page, scrape, move back, repeat)
# for link in links_list:
#     link.click()
#     author = driver.find_element(By.XPATH, "//div[contains(@class,'mb-4')]//a[@href]") # Scrape author data
#     # author = WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'mb-4')]//a[@href]")))
#     #? /html/body/div[1]/main/div/div[2]/article/div[2]/a
#     print(author)


for index, val in enumerate(new_links_list):
        #get the links again after getting back to the initial page in the loop
        links_list = driver.find_elements(By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a[@href]")

        #scroll to the n-th link, it may be out of the initially visible area
        actions.move_to_element(links_list[index]).perform()
        links_list[index].click()
        driver.get(val)
        #scrape the data on the new page and get back with the following command
        author = driver.find_element(By.XPATH, "//div[contains(@class,'mb-4')]//a[@href]")
        print(author)
        driver.execute_script("window.history.go(-1)") #you can alternatevely use this as well: driver.back()
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a[@href]")))
        time.sleep(2)

# Prints article headline text
link_strings = []
for link in links_list:
    link = link.text
    link_strings.append(link)
    print(link_strings)

# for link in link_strings:
#     driver.get(link) # Open tabs for each link
#     author = driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div[2]/article/div[2]/a').click()
#     print(author)






#TODO: Click on Page 2 Button, repeat actions above
#TODO: Loop for each 'News' subsection (DeFi, TradFi, Blockchains, etc.)
#TODO: driver.switchTo().alert().dismiss(); for popups (this is javascript I think but maybe okay)

#TODO: Change to openpyxl format