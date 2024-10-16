from selenium import  webdriver
import allure
import pytest
import time

@allure.title("Verify the title of the webpage.")
#In selenium 4 - driver download by itself..
def test_sample():
    driver=webdriver.Edge()
    driver.get("https://www.google.com/")
    time.sleep(5)

