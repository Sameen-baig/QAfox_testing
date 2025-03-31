from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

#Registration page
driver.get('http://tutorialsninja.com/demo/index.php?route=account/register')
time.sleep(2)

#Registration details
driver.find_element(By.ID, 'input-firstname').send_keys('Testing')
driver.find_element(By.ID, 'input-lastname').send_keys('web')
driver.find_element(By.ID, 'input-email').send_keys('testing123@test.com')  # Use a unique email
driver.find_element(By.ID, 'input-telephone').send_keys('1234567890')
driver.find_element(By.ID, 'input-password').send_keys('test123')
driver.find_element(By.ID, 'input-confirm').send_keys('test123')
time.sleep(1)

#Privacy policy
driver.find_element(By.NAME, 'agree').click()
time.sleep(1)

driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
time.sleep(2)

if "Your Account Has Been Created!" in driver.page_source: #Check if registration is successful
    print("Registration successful!")
else:
    print("Registration failed!")

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

#Wish List
driver.get('http://tutorialsninja.com/demo/index.php?route=account/wishlist')
time.sleep(2)

if "Your wish list is empty." in driver.page_source:
    print("Wish list is empty!")
else:
    print("Wish list contains items!")

#Order History
driver.get('http://tutorialsninja.com/demo/index.php?route=account/order')
time.sleep(2)

if "You have not made any previous orders!" in driver.page_source:
    print("No order history found!")
else:
    print("Order history displayed!")
    
driver.quit()


