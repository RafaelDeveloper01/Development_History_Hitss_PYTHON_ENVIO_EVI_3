#librerias de chrome para selenium y algunas mas de ayuda
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#unaopcion_para_enviar_msj_al_Wsp_(no usada)
import pywhatkit
#control local
import keyword
import pyautogui as pa
#numero o valor aleatorio
import random
#retraso
import time
#libreria_tiempo y suma de tiempo a la hora actual
from datetime import datetime, timedelta
import pytz
import os
from selenium.common.exceptions import NoSuchElementException
import glob
import subprocess
###########################################################################################################################
#### INSTANCIA PRINCIPAL DE CHROME ###
# Crear una instancia de ChromeOptions----------------------
options = Options()
# Agregar la ruta de la extensión a las opciones de Chrome--

options.add_argument("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\CHROME_EXT_EXE\\chromedriver.exe")
# Abrir el navegador completo-------------------------------
options.add_argument("--start-maximized")
# Inicializar el controlador de Chrome con las opciones-----
driver = webdriver.Chrome(options=options)
############################################################################################################################
############################################################################################################################
############################################################################################################################


# Abrir la primera página
driver.get("primera_pagina")
time.sleep(5)
#################################Se tiene modificar en algun momento
#DIGITAR USUARIOS EN LA PRINCIPAL
usuario = driver.find_element(By.ID, "username")
usuario.send_keys("user")
time.sleep(2)
usuario = driver.find_element(By.ID, "password")
usuario.send_keys("pass")
usuario.send_keys(Keys.ENTER)
time.sleep(10)
##################################################################
#ZOOM
driver.execute_script("document.body.style.zoom = '60%'")
time.sleep(15)
driver.execute_script("window.scrollTo(0, 500);")
time.sleep(8)
#CAPTURA GENERAL 
driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_0_1.jpg")
time.sleep(3)

############################################################################################################################
############################################################################################################################

#Link Monitoreo 1
driver.get("primera_pagina2")
time.sleep(5)
toglee = driver.find_element(By.XPATH, '//*[@id="accordionSidebar"]/ul/li[7]/a')
toglee.click()
time.sleep(2)
toglee = driver.find_element(By.XPATH, '//*[@id="collapseIntegracion"]/div/a[1]')
toglee.click()
time.sleep(10)
#zoom_pagina
driver.execute_script("document.body.style.zoom = '65%'")
###

driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_0_2.jpg")
time.sleep(5)
###
driver.execute_script("document.body.style.zoom = '100%'")
time.sleep(5)
#driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_0_2.jpg")
#time.sleep(5)
#Segunda img de la misma pagina click's para llegar 2
toglee = driver.find_element(By.XPATH, '//*[@id="accordionSidebar"]/ul/li[9]/a')
toglee.click()
time.sleep(2)
toglee = driver.find_element(By.XPATH, '//*[@id="collapseApps"]/div/a')
toglee.click()
time.sleep(10)
#DIRIGIRME A LA PARTE DE LA PAGINA QUE QUIERO TOMAR IMG
driver.execute_script("document.body.style.zoom = '80%'")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 410);")
time.sleep(3)
#Encontrar las partes a tomar imagenes
driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_0_3_1.jpg")
time.sleep(5)
###
driver.execute_script("document.body.style.zoom = '100%'")
time.sleep(5)

#Tomar img otra seccion de la misma pagina de monitoreo 3
toglee = driver.find_element(By.XPATH, '//*[@id="accordionSidebar"]/ul/li[5]/a')
toglee.click()
time.sleep(2)
toglee = driver.find_element(By.XPATH, '//*[@id="collapseBSS"]/div/a[3]')
toglee.click()
time.sleep(2)
toglee = driver.find_element(By.XPATH, '//*[@id="collapseprepago"]/div/a[1]')
toglee.click()
time.sleep(5)
driver.execute_script("document.body.style.zoom = '90%'")
time.sleep(15)
driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_4_0.jpg")
time.sleep(3)
driver.close()
time.sleep(8)
#Actulizar via shell para la img 4
# Ruta al programa que deseas abrir

# Ruta al acceso directo que deseas abrir
#ruta_acceso_directo = 'C:/Users/Orlando/Desktop/Mtputty_APP.lnk'

# Abrir el acceso directo
#subprocess.Popen(ruta_acceso_directo)

#time.sleep(2)
#pa.click(x=750, y=300) 
#time.sleep(2)
#pa.press('enter')
pa.hotkey("ctrl", "alt", "o")
time.sleep(10)
pa.hotkey("ctrl", "k")
time.sleep(5)
pa.write("172.19.30.62") 
pa.press("Tab")
time.sleep(5)
pa.press("Tab")
pa.write("22") 
time.sleep(5)
pa.press("enter")
time.sleep(5)
pa.write("pbscs7") 
time.sleep(5)
pa.press("enter")
time.sleep(5)
ruta_archivo="C:/Automatizacion_PYTHON_ENTORNO_IMG/BOT_IMAGEN_3_VR/contraseñas/contraseña.txt"
subprocess.Popen(["notepad.exe",ruta_archivo])
time.sleep(2)
pa.hotkey('ctrl', 'e')
time.sleep(2)
pa.hotkey('ctrl', 'c')
time.sleep(2)
pa.hotkey('alt','f4')
time.sleep(5)
pa.rightClick(500, 500)
time.sleep(2)
pa.press('enter')
time.sleep(10)
pa.typewrite('/bscs70/bscs/work/OPERA/CANVIA_CONTROLES/SH_CIERRE_TRAFICO.sh')
time.sleep(2)
pa.press('enter')
time.sleep(20)
#subprocess.call(['taskkill', '/F', '/IM', ruta_pro])
pa.hotkey("Alt", "f4")
time.sleep(2)
pa.press('enter')
time.sleep(2)
pa.hotkey("Alt", "f4")
time.sleep(6)


############################################################################################################################
#### INSTANCIA PRINCIPAL DE CHROME ###
# Crear una instancia de ChromeOptions----------------------
options = Options()
# Agregar la ruta de la extensión a las opciones de Chrome--

options.add_argument("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\CHROME_EXT_EXE\\chromedriver.exe")
# Abrir el navegador completo-------------------------------
options.add_argument("--start-maximized")
# Inicializar el controlador de Chrome con las opciones-----
driver = webdriver.Chrome(options=options)
#volver a abrir la pagina
driver.get("primera_pagina3")
time.sleep(5)
#Tomar img otra seccion de la misma pagina de monitoreo 4
toglee = driver.find_element(By.XPATH, '//*[@id="accordionSidebar"]/ul/li[5]/a')
toglee.click()
time.sleep(2)
toglee = driver.find_element(By.XPATH, '//*[@id="collapseBSS"]/div/a[2]')
toglee.click()
time.sleep(2)
toglee = driver.find_element(By.XPATH, '//*[@id="collapsepostmain"]/div/a[2]')
toglee.click()
time.sleep(10)
#zoom_pagina
driver.execute_script("document.body.style.zoom = '70%'")
time.sleep(5)
driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_4_1.jpg")
time.sleep(5)
driver.close()
time.sleep(5)

##############################################################################################################
##############################################################################################################
options = Options()
# Agregar la ruta de la extensión a las opciones de Chrome--

options.add_argument("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\CHROME_EXT_EXE\\chromedriver.exe")
# Abrir el navegador completo-------------------------------
options.add_argument("--start-maximized")
# Inicializar el controlador de Chrome con las opciones-----
driver = webdriver.Chrome(options=options)
#volver a abrir la pagina
driver.get("hprimera_pagina5")
time.sleep(5)
driver.execute_script("document.body.style.zoom = '150%'")
time.sleep(5)
driver.execute_script("window.scrollTo(0, 5000);")
time.sleep(2)
driver.execute_script("window.scrollTo(0, 5000);")
time.sleep(10)
driver.save_screenshot("C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3\\IMG_5.jpg")
time.sleep(5)
driver.close()
#
time.sleep(5)
############################################################################################################################
############################################################################################################################
############################################################################################################################
############################################################################################################################
#####################################################ENVIO_WSP###
#CARPETA_ORIGEN_GUARDA_ARCHIVOS_de a ca sacare los archivos que enviare por wsp
carpeta_imagenes = "C:\\Automatizacion_PYTHON_ENTORNO_IMG\\BOT_IMAGEN_3_VR\\IMG_ENVIO_WSP_VR3"

#################################### INSTANCIA SECUNDARIA DE CHROME PARA WSP__inicio##########################################

# Ruta al perfil de Chrome que deseas utilizar(dependencia_aparte)
profile_path = r"ruta_de_perfil"

# Configurar las opciones del navegador para utilizar el perfil
options.add_argument("--user-data-dir=" + profile_path)

# Reutilizar la instancia de Chrome con el perfil seleccionado(Profile 1)
driver = webdriver.Chrome(options=options)
time.sleep(5)

#################################### INSTANCIA SECUNDARIA DE CHROME PARA WSP__fin##########################################

#Seleccion_link
driver.get("https://web.whatsapp.com/")
time.sleep(35)

#Seleccionar la barra buscadora de wsp y buscar el nombre del grupo
Click_wsp = driver.find_element(By.CSS_SELECTOR, "div._3gYev > div > div._1EUay > div._2vDPL > div > div.to2l77zo.gfz4du6o.ag5g9lrv.bze30y65.kao4egtt.qh0vvdkp > p")
Click_wsp.click()
#Name_grup
Click_wsp.send_keys("equipo")
Click_wsp.send_keys(Keys.ENTER)
time.sleep(3)

#Bucle para el envio consecutivo de las img alojadas en una carpeta
for imagen in os.listdir(carpeta_imagenes):
    ruta_imagen = os.path.join(carpeta_imagenes, imagen)
    #selecionar lo adjunto
    attachment_button = driver.find_element(By.XPATH,'//div[@title="Adjuntar"]')
    attachment_button.click()
    time.sleep(3)
    #elegir el tipo de archivo que se desea enviar
    file_input = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    file_input.send_keys(ruta_imagen)
    time.sleep(3)
    #selecion de icono (adjuntador"+"")
    send_button = driver.find_element(By.XPATH,'//span[@data-icon="send"]')
    send_button.click()
    time.sleep(3)
driver.close()
time.sleep(5)