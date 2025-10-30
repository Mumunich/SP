from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

WebDriverWait(driver, 20).until(
    lambda driver: len(driver.find_elements(By.TAG_NAME, "img")) == 4
    and all(
        img.get_attribute("src")
        for img in driver.find_elements(By.TAG_NAME, "img")
    )
)

images = driver.find_elements(By.TAG_NAME, "img")
third_src = images[2].get_attribute("src")

print(third_src)

driver.quit()
