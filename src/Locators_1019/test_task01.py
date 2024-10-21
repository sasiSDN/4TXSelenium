import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


@allure.title("verify the register page")
@allure.description("Verify that register page, fill the details")
def test_register():
    driver=webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")
    element_first_name=driver.find_element(By.XPATH,"//input[@name='firstname']")
    element_first_name.send_keys("sasi")
    element_last_name=driver.find_element(By.XPATH,"//input[@name='lastname']")
    element_last_name.send_keys("naidu")
    element_email=driver.find_element(By.XPATH,"//input[@placeholder='E-Mail']")
    element_email.send_keys("Abc323234311@gmail.com")
    element_mobile=driver.find_element(By.XPATH,"//input[@placeholder='Telephone']")
    element_mobile.send_keys("3244242424")
    element_password=driver.find_element(By.XPATH,"//input[@id='input-password']")
    element_password.send_keys("sdfag123")
    element_password2=driver.find_element(By.XPATH,"//input[@id='input-confirm']")
    element_password2.send_keys("sdfag123")
    element_Tnc=driver.find_element(By.XPATH,"//input[@name='agree']")
    element_Tnc.click()
    element_submit=driver.find_element(By.XPATH,"//input[@value='Continue']")
    element_submit.click()
    time.sleep(3)
    assert driver.title=="Your Account Has Been Created!"
