
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

try:
 #interacciones
    productos = driver.find_element(By.CLASS_NAME,"inventory_item")
    productos[0].find_element(By.TAG_NAME,"button").click()
    productos[0]
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"

 
finally:
    driver.quit()