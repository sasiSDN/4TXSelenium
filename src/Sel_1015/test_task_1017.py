from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def test_login():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element=driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"
    log_element=driver.find_element(By.ID,"txt-username")
    log_element.send_keys("John Doe")
    pas_element=driver.find_element(By.ID,"txt-password")
    pas_element.send_keys("ThisIsNotAPassword")
    sub_element=driver.find_element(By.ID,"btn-login")
    sub_element.click()
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/#appointment"