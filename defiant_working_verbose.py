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
print(hot_topics)

topics_list = []
for topic in hot_topics:
    print(topic.text)


# Close the WebDriver instance
driver.quit()

