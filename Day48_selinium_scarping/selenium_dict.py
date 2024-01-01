from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
 
# Navigate to the Wikipedia page
driver.get("https://www.python.org/")

event_time = driver.find_elements(By.CSS_SELECTOR, ".event-widget.last time")
# for times in event_time:
#     (times.text)

event_name = driver.find_elements(By.CSS_SELECTOR, ".event-widget.last li a")
# for times in event_time[1:]:
#     print(times.text)

dict = {} 

for n in range(len(event_time)):
    dict[n] = {
        "time" : event_time[n].text,
        "name" : event_name[n].text
    }

print(dict)


driver.quit()
