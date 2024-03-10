from Abrir import Abrir
from Inicio import Selects
from IDcolegios import ListaColegiosID
from DatosColegio import DatosUnicos

import itertools
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



Localidades = list(range(1,3))

driver = Abrir()
wait = WebDriverWait(driver, 5)
Ids=[]


for localidad in Localidades:
    driver.get('https://dueb.educacionbogota.edu.co/Dueb/')
    Selects(driver,localidad)
    

    PrimerListaWeb = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@href, '/Dueb/colegioEdit.sed?id=')]")))
    
    PrimerListaColegios=[]

    for elemento in PrimerListaWeb:
        PrimerListaColegios.append(elemento.get_attribute('href'))
    
    
    Ids.append(ListaColegiosID(driver,PrimerListaColegios))
    print(PrimerListaColegios)
    sleep(1)

lista_unificada = list(itertools.chain(*Ids))
print(lista_unificada)
print(len(lista_unificada))    
DatosUnicos(driver, lista_unificada)
    


#sleep(1)
