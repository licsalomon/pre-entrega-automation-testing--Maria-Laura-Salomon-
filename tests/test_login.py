
def test_login_validation(login_in_driver):
    try:
     #login
        driver = login_in_driver
    

     #validación de la redirección de la página
        assert "/inventory.html" in driver.current_url, "No se redirgio al inventario"
        
     #Tratamiento de errores
    except Exception as e:
        print(f"Error en test_login: {e}")
        raise
    finally:
        driver.quit()
        



    
    