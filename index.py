from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

try:
    #titulo
    driver.get("https://www.saucedemo.com/")
    print("Titulo:",driver.title)
    assert driver.title == "Swag Labs"
    time.sleep(2)

    #login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)

    #validación de la redirección de la página
    assert "/inventory.html" in driver.current_url

    #interacciones
    productos = driver.find_element(By.CLASS_NAME,"inventory_item")
    productos[0].find_element(By.TAG_NAME,"button").click()
    productos[0]
    carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert carrito == "1"

    print("Test OK")
 
finally:
    driver.quit()