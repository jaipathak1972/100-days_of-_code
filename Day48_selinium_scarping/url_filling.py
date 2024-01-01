import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://secure-retreat-92358.herokuapp.com/")
driver.maximize_window()

name =driver.find_element(By.NAME,"fName")
last_name =driver.find_element(By.NAME,"lName")
email = driver.find_element(By.NAME,"email")

name.send_keys("Jai")
last_name.send_keys("Pathak")
email.send_keys("jaipathak1972@gmail.com")


enter = driver.find_element(By.XPATH,"/html/body/form/button")

enter.send_keys(Keys.ENTER)

