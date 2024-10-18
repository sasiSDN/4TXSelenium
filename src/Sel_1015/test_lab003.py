from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def test_chrome_options():
    chrome_options=Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--window-size=900,400")
    # chrome_options.add_argument("--headless")

    driver=webdriver.Chrome(chrome_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")

def test_Edge_options():
    Edge_options = Options()
    driver = webdriver.Edge(Edge_options)
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    time.sleep(5)