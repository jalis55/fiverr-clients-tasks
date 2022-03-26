from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

#open the webpage
driver.get("https://pythonsandbox.com/")

#run code

run=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button [@class='btn btn-info runner']"))).click()