from Util import Util
import requests
from selenium import webdriver
import time
import datetime


lista_emails = ["fczb_btc0@outlook.es",
                "carloszaragozabeato15@gmail.com",
                "carloszaragozabeato@gmail.com",
                "carloszaragoza716@gmail.com",
                "fczb_btc1@outlook.es"]











# # '//*[@id="free_play_form_button"]'
def algoritmo_roll(driver, index):
    util = Util(driver=driver)
    util.driver.get("https://freebitco.in/")




    
    tiempo = 40

    
    if index == 0:
        tiempo = 40
    
    
    
    
    
    time.sleep(tiempo)
    # if server_condition:
    xpath_puntos = "/html/body/div[1]/div/nav/section/ul/li[20]/span"
    hora = datetime.datetime.now()
    xpath_puntos_obtenidos = "/html/body/div[2]/div/div/div[7]/div[3]/div/span[1]"
    
    puntos_obtenidos = util.obtenerXpath(xPath=xpath_puntos_obtenidos).text
    email = lista_emails[index]
    saldo_actual = util.obtenerXpath(xPath=xpath_puntos).text
    
    url = f"http://127.0.0.1:8000/update/?saldo_actual={saldo_actual}&recogida={puntos_obtenidos}&email={email}"
    response = requests.get(url)
    




    util.driver.close()
    
    
for index in range(5): 
    options = webdriver.FirefoxOptions()
    ruta = f"/home/carlos/snap/firefox/common/.mozilla/firefox/{index+1}"
    options.profile = ruta 
    driver = webdriver.Firefox(options=options)
    algoritmo_roll(driver, index)


