from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
 
# Navigate to the Wikipedia page
driver.get("https://en.wikipedia.org/wiki/Blog")

# Use the class name to locate the element
element = driver.find_element(By.CLASS_NAME, "hatnote.navigation-not-searchable")
element2 = driver.find_element(By.XPATH, '/html/body/a[1]')

# Extract the text from the element
text = element.get_attribute()
text2 = element2.text

# Print the text
print(text2)


# Quit the driver when done
driver.quit()
