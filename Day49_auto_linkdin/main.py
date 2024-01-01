import time
from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

time.sleep(2)

# Locate the "Sign in" button using a CSS selector
sign_in_button = driver.find_element(By.CLASS_NAME,"cta-modal__primary-btn")
sign_in_button.click()
        
time.sleep(2)
    
# Find the email and password input fields
email = driver.find_element(By.NAME, "session_key")
password = driver.find_element(By.NAME, "session_password")
    
email.send_keys("jaipathak1972@gmail.com")
password.send_keys("jaipathak2005")
    
click = driver.find_element(By.CSS_SELECTOR, "div.login__form_action_container button")
click.click() 
time.sleep(2)

link = driver.find_element(By.CSS_SELECTOR, 'full-width.artdeco-entity-lockup__title.ember-view a.disabled ember-view ')

link.click()
    
time.sleep(2)
    
# Apply button should be located using its ID without the #
apply_btn = driver.find_element(By.CSS_SELECTOR, "div.jobs-apply-button--top-card button")
apply_btn.click()

time.sleep(2)
    
# Apply button should be located using its ID without the #
# summery = driver.find_element(By.CSS_SELECTOR, "div.ember-view textarea")

# summery.send_keys("hello its just a test")

