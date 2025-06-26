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

campos = driver.find_element(By.CLASS_NAME, "input_error form_input") # Los campos username y password tiene la misma nombre de clase, por lo que se crea un arreglo.

username = campos[0] # En la posición 0 se guarda el primer input que es el del nombre de usuario
password = campos[1] # En la posición 1 se guarda el segundo input que es el de la contraseña

print("es correcto")

