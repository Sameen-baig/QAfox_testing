from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

#Login page
driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')
time.sleep(2)

#Enter email and password
driver.find_element(By.ID, 'input-email').send_keys('testing11@test.com')  # Replace with your actual email
driver.find_element(By.ID, 'input-password').send_keys('test123')          # Replace with your actual password

#Login button
driver.find_element(By.XPATH, '//input[@value="Login"]').click()
time.sleep(2)

# Check if login is successful
if "My Account" in driver.title:
    print("Login successful!")

    # Click on My Account dropdown
    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    time.sleep(1)

    # Click Logout
    driver.find_element(By.LINK_TEXT, 'Logout').click()
    time.sleep(2)

    # Verify logout
    if 'Account Logout' in driver.page_source:
        print("Logout successful!")
    else:
        print("Logout failed!")
else:
    print("Login failed!")

# Close the browser
driver.quit()

#login and logout, verify logout