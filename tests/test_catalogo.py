
import time
from selenium.webdriver.common.by import By

def test_catalogo(login_in_driver):
    try:
     #login
        driver = login_in_driver 

     #Título de la página
        assert driver.title == 'Swag Labs', 'El titulo no es el correcto'
 
     #Verificar productos visibles
        productos = driver.find_elements(By.CLASS_NAME, 'inventory_item')
        print(f'Se encontraron {len(productos)} productos.')

      #Capturar nombre y precio del primer producto
        primerNombre  = productos[0].find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        primerPrecio = productos[0].find_element(By.CSS_SELECTOR, '.inventory_item_price').text
        print(f'Primer producto: {primerNombre} – {primerPrecio}')

     #Verificar filtro
        driver.find_element(By.CLASS_NAME,'product_sort_container').click()
        time.sleep(2)

     #Verificar menu
        driver.find_element(By.CLASS_NAME,'bm-burger-button').click()
        time.sleep(2)
        linkMenu = driver.find_element(By.ID, 'inventory_sidebar_link')
        assert linkMenu.is_displayed(), 'Menu no encontrado'
        driver.find_element(By.CLASS_NAME,'bm-cross-button').click

      #Tratamiento de errores
    except Exception as e:
        print(f"Error en test_catalogo: {e}")
        raise
    
    finally:
        driver.quit()