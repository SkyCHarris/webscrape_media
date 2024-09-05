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
time.sleep(3) 

# Get list of article links (as web elements)

links_list = [link for link in driver.find_elements(By.XPATH, "//section[@class='mt-4']/div//div[@class='flex flex-col']/a[@href]")]
print(links_list)



#TODO: Loop for each 'News' subsection (DeFi, TradFi, Blockchains, etc.)
#TODO: Click on Page 2 Button, repeat actions above
#TODO: driver.switchTo().alert().dismiss(); for popups (this is javascript I think but maybe okay)

#TODO: Change to openpyxl format
