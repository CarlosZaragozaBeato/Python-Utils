from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#### Clase que heredaran cada una de las clases hijas para ahorrar lineas de codigo
class Util:
    def __init__(self, driver):
        self.driver = driver
        self.wait1 = WebDriverWait(self.driver, 15)
        
    
    def ObtenerListaElementos(self, xPath:str):
        return self.wait1.until(EC.presence_of_all_elements_located((
                By.XPATH, xPath)))

    def ObtenerListaElementosClassName(self, className:str):
        return self.wait1.until(EC.presence_of_all_elements_located((
                By.CLASS_NAME, className)))
    
    def obtenerXpath(self, xPath:str):
        return self.wait1.until(EC.presence_of_element_located((
                By.XPATH, xPath)))
        
    def obtenerClassName(self, ClassName):
        return self.wait1.until(EC.presence_of_element_located((
                By.CLASS_NAME, ClassName)))
    
    def obtenerCssSelector(self, cssSelector):
        return self.wait1.until(EC.presence_of_all_elements_located((
            By.CSS_SELECTOR, cssSelector
        )))
        
    def obtener_uno_CssSelector(self, cssSelector):
        return self.wait1.until(EC.presence_of_element_located((
            By.CSS_SELECTOR, cssSelector
        )))
        
    def obtenerClassNames(self, ClassName):
        return self.wait1.until(EC.presence_of_all_elements_located((
                By.CLASS_NAME, ClassName)))