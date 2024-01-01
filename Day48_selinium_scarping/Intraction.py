import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chome_option = webdriver.ChromeOptions()
chome_option.add_experimental_option("detach", True )
driver = webdriver.Chrome(options=chome_option)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.maximize_window()

# number = driver.find_element(By.XPATH , '//*[@id="articlecount"]/a[1]')
# number.click()

# all_portals = driver.find_element(By.LINK_TEXT, "View source")
# all_portals.click()
# all_portals = driver.find_element(By.LINK_TEXT, "View history")
# all_portals.click()

search = driver.find_element(By.NAME ,'search')
search.send_keys("hello")
search.send_keys(Keys.ENTER)
# driver.quit()