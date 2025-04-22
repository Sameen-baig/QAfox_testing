from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()


driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

driver.find_element(By.ID, "input-email").send_keys("your_email@example.com")
driver.find_element(By.ID, "input-password").send_keys("wrongpassword")
driver.find_element(By.CSS_SELECTOR, "input[value='Login']").click()
time.sleep(2)

if "Warning: No match for E-Mail Address and/or Password." in driver.page_source:
    print("✅ Wrong Password Login: PASSED")
else:
    print("❌ Wrong Password Login: FAILED")

driver.save_screenshot("wrong_password_login.png")
driver.quit()


driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

driver.find_element(By.ID, "input-firstname").send_keys("Ali")
driver.find_element(By.ID, "input-lastname").send_keys("Khan")
driver.find_element(By.ID, "input-email").send_keys("your_email@example.com")  # Already registered
driver.find_element(By.ID, "input-telephone").send_keys("1234567890")
driver.find_element(By.ID, "input-password").send_keys("password123")
driver.find_element(By.ID, "input-confirm").send_keys("password123")
driver.find_element(By.NAME, "agree").click()
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

if "Warning: E-Mail Address is already registered!" in driver.page_source:
    print("✅ Existing Email Registration: PASSED")
else:
    print("❌ Existing Email Registration: FAILED")

driver.save_screenshot("existing_email_registration.png")
driver.quit()


driver = webdriver.Chrome()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

# Only fill in first name
driver.find_element(By.ID, "input-firstname").send_keys("Ali")
driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
time.sleep(2)

if "First Name must be between 1 and 32 characters!" not in driver.page_source:
    print("✅ Incomplete Form Submission: PASSED (validation working)")
else:
    print("❌ Incomplete Form Submission: FAILED")

driver.save_screenshot("incomplete_form_submission.png")
driver.quit()

#incomplete_form, existing email, wrong password login