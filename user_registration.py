from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# Unique email using timestamp
unique_email = f'testing_{int(time.time())}@test.com'

try:
    # Registration
    driver.get('http://tutorialsninja.com/demo/index.php?route=account/register')
    time.sleep(2)
    driver.find_element(By.ID, 'input-firstname').send_keys('Testing')
    driver.find_element(By.ID, 'input-lastname').send_keys('web')
    driver.find_element(By.ID, 'input-email').send_keys(unique_email)
    driver.find_element(By.ID, 'input-telephone').send_keys('1234567890')
    driver.find_element(By.ID, 'input-password').send_keys('test123')
    driver.find_element(By.ID, 'input-confirm').send_keys('test123')
    driver.find_element(By.NAME, 'agree').click()
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    time.sleep(2)

    if "Your Account Has Been Created!" in driver.page_source:
        print("✅ Registration successful!")
    else:
        print("Registration failed!")

    # Logout to test forgotten password
    driver.get('http://tutorialsninja.com/demo/index.php?route=account/logout')
    time.sleep(1)

    # Forgotten Password
    driver.get('http://tutorialsninja.com/demo/index.php?route=account/forgotten')
    time.sleep(1)
    driver.find_element(By.ID, 'input-email').send_keys(unique_email)
    driver.find_element(By.XPATH, '//input[@value="Continue"]').click()
    time.sleep(2)

    if "An email with a confirmation link has been sent" in driver.page_source:
        print("✅ Password reset email sent!")
    else:
        print("Password reset failed!")

    # Login again to access wish list & orders
    driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')
    driver.find_element(By.ID, 'input-email').send_keys(unique_email)
    driver.find_element(By.ID, 'input-password').send_keys('test123')
    driver.find_element(By.XPATH, '//input[@value="Login"]').click()
    time.sleep(2)

    # Wish List
    driver.get('http://tutorialsninja.com/demo/index.php?route=account/wishlist')
    time.sleep(1)
    if "Your wish list is empty." in driver.page_source:
        print("✅ Wish list is empty!")
    else:
        print("Wish list has items!")

    # Order History
    driver.get('http://tutorialsninja.com/demo/index.php?route=account/order')
    time.sleep(1)
    if "You have not made any previous orders!" in driver.page_source:
        print("✅ No order history found!")
    else:
        print("Order history displayed!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()


#user registration, Forgotten Password, Wish List, Order History
