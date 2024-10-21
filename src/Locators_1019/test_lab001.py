import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
@allure.description("verify that email/password is wrong,display text message")
def test_negative_vwo_url():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    log_element=driver.find_element(By.ID,"login-username")
    log_element.send_keys("abc@gmail.com")
    pass_element=driver.find_element(By.NAME,"password")
    pass_element.send_keys("Password@1234")
    submit=driver.find_element(By.ID,"js-login-btn")
    submit.click()
    time.sleep(3)
    error_element=driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_element.text)
    assert error_element.text == "Your email, password, IP address or location did not match"
    time.sleep(4)