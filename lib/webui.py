from selenium import webdriver
import time

from selenium.webdriver.common.by import By


def loginAndCheck(username,password):
    driver = webdriver.Chrome()
    driver.implicitly_wait(2)
    driver.get('http://127.0.0.1/mgr/sign.html')
    if username is not None:
        driver.find_element(By.ID,'username').send_keys(username)
    if password is not None:
        driver.find_element(By.ID,'password').send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    time.sleep(2)
    alertText =  driver.switch_to.alert.text
    print(alertText)
    driver.quit()
    return alertText
