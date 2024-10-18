import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def test_verify_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    element=driver.find_element(By.ID,"btn-make-appointment")
    element.click()
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"
    time.sleep(3)