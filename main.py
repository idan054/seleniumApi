from selenium import webdriver
import os

## Ready or Heroku deploy.

chrome_options = webdriver.options()
# options.add_argument("--window-size=1100,900")
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
browser = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

# Now you can start using Selenium
browser.get("https://google.com")
print(browser.title)

