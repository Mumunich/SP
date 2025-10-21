from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/inputs")
driver.find_element(By.TAG_NAME, "input").send_keys("Sky")
sleep(2)
driver.find_element(By.TAG_NAME, "input").clear()
sleep(2)
driver.find_element(By.TAG_NAME, "input").send_keys("Pro")
sleep(2)
driver.quit()
