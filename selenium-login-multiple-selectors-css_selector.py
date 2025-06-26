from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Usar el servicio de ChromeDriver
service = Service('./chromedriver.exe')  # Asegúrate del nombre y ubicación

# Crear el navegador
driver = webdriver.Chrome(service=service)

# Abrir el sitio
driver.get("https://www.saucedemo.com/")
time.sleep(2)

# Encontramos los input del login mediante CSS selector
#username = driver.find_element(By.CSS_SELECTOR, "#user-name") # primero ubicamos el input y lo guardamos en una variable
#password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password']") # ubicamos el input de password y lo guardamos en una variable

campos = driver.find_elements(By.CSS_SELECTOR, ".form_input")
username = campos[0]
password = campos[1]
# Escribimos en los inputs

username.send_keys("standard_user")
password.send_keys("secret_sauce")

# Damos clic el botón Login
time.sleep(2)
loginbutton = driver.find_element(By.ID, "login-button") # primero ubicamos el input y lo guardamos en una variable
loginbutton.click() 

# Validamos que el login fue correcto buscando el elemento Products
validarlogin = driver.find_element(By.CLASS_NAME, "title")
assert validarlogin.text == "Products"
time.sleep(2)
print("✅ El login es correcto")