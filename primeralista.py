from time import sleep
from Inicio import Selects
from IDcolegios import ListaColegiosID
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

IdsBuenos=[]
IdsMalos=[]


def PrimerLista(driver,localidades):

    wait = WebDriverWait(driver, 5)

    for localidad in localidades:
        driver.get('https://dueb.educacionbogota.edu.co/Dueb/')
        Selects(driver,localidad)
        

        PrimerListaWeb = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@href, '/Dueb/colegioEdit.sed?id=')]")))
        
        PrimerListaColegios=[]

        for elemento in PrimerListaWeb:
            PrimerListaColegios.append(elemento.get_attribute('href'))
        
        Buenos,malos=ListaColegiosID(driver,PrimerListaColegios)
        IdsBuenos.append(Buenos)
        IdsMalos.append(malos)
        print(PrimerListaColegios)
        print('//////////////////////////Colegios malos//////////////////////////////////////////')
        print(malos)
        sleep(1)
    
    return IdsBuenos,malos