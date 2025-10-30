from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)
driver.get("http://uitestingplayground.com/textinput")
input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")
driver.find_element(By.ID, "updatingButton").click()
wait.until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)
updated_button = driver.find_element(By.ID, "updatingButton")
print(updated_button.text)
driver.quit()
