# Proyecto de Automatización de Pruebas

## Propósito del proyecto

Este proyecto tiene como objetivo automatizar pruebas funcionales para la página [SauceDemo](https://www.saucedemo.com/) utilizando Selenium y Pytest. Incluye casos de prueba para login, catálogo de productos y carrito de compras, generando reportes HTML detallados.

## Tecnologías utilizadas

- Python 3.13
- Selenium
- Pytest
- Pytest-HTML

## Instrucciones de instalación de dependencias

1. Clona el repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando:

```sh
pip install -r requirements.txt
```

Si no tienes un archivo `requirements.txt`, instala manualmente:

```sh
pip install selenium pytest pytest-html
```

## Comando para ejecutar las pruebas

Puedes ejecutar todas las pruebas y generar el reporte HTML con el siguiente comando:

```sh
pytest -v --html=reports/report.html --self-contained-html
```

O ejecuta el script incluido:

```sh
python run_tests.py
```

El reporte se guardará en la carpeta `reports` como `report.html`.