import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Login and Logout Test")
@allure.description("This test logs in with valid credentials and verifies logout.")
def test_login_logout():
    driver = webdriver.Chrome()
    driver.maximize_window()

    driver.get('http://tutorialsninja.com/demo/index.php?route=account/login')
    time.sleep(2)

    driver.find_element(By.ID, 'input-email').send_keys('testing11@test.com')
    driver.find_element(By.ID, 'input-password').send_keys('test123')
    driver.find_element(By.XPATH, '//input[@value="Login"]').click() #login
    time.sleep(2)

    assert "My Account" in driver.title, "Login failed!"

    driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    time.sleep(1)

    driver.find_element(By.LINK_TEXT, 'Logout').click() #logout
    time.sleep(2)

    assert 'Account Logout' in driver.page_source, "Logout failed!"

    driver.quit()
    
#login and logout, verify logout
#allure reporing also added
