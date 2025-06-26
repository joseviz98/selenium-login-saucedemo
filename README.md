# 🧪 Automatización de Login – Selenium con múltiples selectores

Este repositorio contiene 4 scripts de automatización del login en [saucedemo.com](https://www.saucedemo.com), utilizando diferentes estrategias de selección de elementos con Selenium en Python.

Cada script realiza exactamente la misma prueba:  
✅ Llenar el formulario de inicio de sesión  
✅ Validar que el login fue exitoso  
✅ Imprimir un mensaje de confirmación

---

## 🚀 Sitio de prueba

- **URL:** https://www.saucedemo.com  
- **Usuario:** `standard_user`  
- **Contraseña:** `secret_sauce`

---

## ⚙️ Herramientas utilizadas

- Python 3
- Selenium
- Google Chrome + ChromeDriver
- Visual Studio Code
- Git & GitHub

---

## 📁 Estructura del repositorio

| Archivo                          | Selector usado     |
|----------------------------------|--------------------|
| `login_by_id.py`                | `By.ID`            |
| `login_by_class_name.py`        | `By.CLASS_NAME`    |
| `login_by_css_selector.py`      | `By.CSS_SELECTOR`  |
| `login_by_xpath.py`             | `By.XPATH`         |

---

## 📌 Objetivo

Demostrar cómo se puede automatizar un mismo flujo usando diferentes estrategias de localización de elementos en Selenium:

- ✔️ Localización por ID
- ✔️ Localización por nombre de clase
- ✔️ Localización por atributos y clases vía CSS Selectors
- ✔️ Localización estructural vía XPath

