import time
from selenium.webdriver.common.by import By

def test_carrito(login_in_driver):
    try:
    #login
        driver = login_in_driver

    #Agregar el primer producto al carrito
        productos = driver.find_elements(By.CLASS_NAME,'inventory_item')
        primerNombre  = productos[0].find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        primerPrecio = productos[0].find_element(By.CSS_SELECTOR, '.inventory_item_price').text
        productos[0].find_element(By.TAG_NAME,'button').click()
        time.sleep(2)

    #Verificar que el producto haya sido agregado y el contador del carrito funcione
        carrito = driver.find_element(By.CLASS_NAME, 'shopping_cart_badge').text
        assert carrito == '1', 'El carrito no funciona'

    #Entrar en el carrito
        driver.find_element(By.CLASS_NAME,'shopping_cart_link').click()
        assert "/cart.html" in driver.current_url, "No se redirgio al carrito"
        time.sleep(2)

    #Verificar que el producto añadido aparezca correctamente
        assert primerNombre == driver.find_element(By.CSS_SELECTOR, '.inventory_item_name').text
        assert primerPrecio == driver.find_element(By.CSS_SELECTOR, '.inventory_item_price').text
   
    #Tratamiento de errores
    except Exception as e:
        print(f"Error en test_carrito: {e}")
        raise
    
    finally:
        driver.quit()