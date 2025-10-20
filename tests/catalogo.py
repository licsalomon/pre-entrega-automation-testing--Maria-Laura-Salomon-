
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

try:
    driver.get("https://www.saucedemo.com/")
     #Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
 
 #Titulo del catálogo
    #titulo = driver.find_element(By.CLASS_NAME,'app_logo').text
    #assert titulo == 'Products'
    #assert driver.find_element(By.CLASS_NAME,'app_logo').text == 'Products'
    #header_title = driver.find_element(By.CSS_SELECTOR,"div.header_secondary_container.title").text
    #assert header_title == "Products", f"Título inesperado: {header_title}"

 #Verificar productos visibles
    productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
    print(f'Se encontraron {len(productos)} productos.')

 #Verificar filtro
    filtro = driver.find_element(By.CLASS_NAME,'product_sort_container').click()
    time.sleep(2)

#Verificar menu
    driver.find_element(By.CLASS_NAME,'bm-burger-button').click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,'bm-cross-button').click
 
finally:
    driver.quit()