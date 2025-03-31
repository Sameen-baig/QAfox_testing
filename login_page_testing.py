from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()
# Open the login page
driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')
time.sleep(2)
# Enter email
email = driver.find_element(By.ID, 'input-email')
email.send_keys('test@test.com')  # Replace with your actual email
# Enter password
password = driver.find_element(By.ID, 'input-password')
password.send_keys('test123')  # Replace with your actual password
# Click the login button
login_button = driver.find_element(By.XPATH, '//input[@value="Login"]')
login_button.click()
time.sleep(2)
# Check if login is successful
if "My Account" in driver.title:
    print("Login successful!")
else:
    print("Login failed!")
# Close the browser
driver.quit()
