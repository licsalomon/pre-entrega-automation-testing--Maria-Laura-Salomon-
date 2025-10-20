from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

try:
 #login
    driver.get("https://www.saucedemo.com/")

    #Título de la página
    titulo = driver.find_element(By.TAG_NAME,"title")
    assert titulo == "Swag Labs", "{titulo} no es el titulo correcto"
    
    #Login
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    time.sleep(2)

    #validación de la redirección de la página
    assert "/inventory.html" in driver.current_url, "Fallo en el redireccionamiento"

#Tratamiento de errores
except Exception as e:
     print(f"Error en test: {e}")
     raise
finally:
     driver.quit()
