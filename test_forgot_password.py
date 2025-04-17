from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

#Forgotten Password
driver.get('http://tutorialsninja.com/demo/index.php?route=account/forgotten')
time.sleep(2)

driver.find_element(By.ID, 'input-email').send_keys('testing123@test.com')
driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
time.sleep(2)
if "An email with a confirmation link has been sent" in driver.page_source:
    print("Password reset email sent successfully!")
else:
    print("Password reset failed!")

#forgotten password