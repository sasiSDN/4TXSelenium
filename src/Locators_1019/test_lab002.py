import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import allure

@allure.title("Positive test case")
@allure.description("Free trail button is clicked,Navigated to next page")
@allure.description("verify that email/password is wrong,display text message")
def test_postive_free_trail():
    driver=webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")
    #Link Test
    # anchor_tag_element=driver.find_element(By.LINK_TEXT,"Start a free trial")
    #partial link test
    anchor_tag_element = driver.find_element(By.PARTIAL_LINK_TEXT, "free trial")
    anchor_tag_element.click()
    time.sleep(3)
    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"
    time.sleep(3)