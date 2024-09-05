from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up a Selenium WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to The Defiant website
url = "https://thedefiant.io/"
driver.get(url)

# Wait for the page to load (optional)
time.sleep(5)  # Adjust the sleep time according to your needs

# Find and extract the hot topics or latest news articles
hot_topics = driver.find_elements(By.CLASS_NAME, "mb-1")
# print(hot_topics)

topics_list = []
for topic in hot_topics:
    title_element = topic.find_element(By.TAG_NAME, "a href")
    title = title_element.text.strip()
    
    link_element = topic.find_element(By.TAG_NAME, "a")
    link = link_element.get_attribute("href")
    
    topics_list.append({"title": title, "link": link})

# Print or store the extracted data as needed

print(topics_list)

# Close the WebDriver instance
driver.quit()

