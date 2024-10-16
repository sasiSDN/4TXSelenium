from selenium import webdriver

def test_verify_url():
    driver=webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/"
    assert driver.title == "CURA Healthcare Service"
    driver.page_source.find("CURA Healthcare Service")

