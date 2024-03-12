import re
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

errores =[]
#continue


def ListaColegiosID(driver,PrimerListaColegios):
    wait = WebDriverWait(driver, 5)
    idColegios=[]

    for elementoLista in PrimerListaColegios:
        driver.get(elementoLista)
        try:
            SegundoListaWeb = wait.until(EC.presence_of_all_elements_located((By.XPATH,"//a[contains(@href, 'javascript:enviar')]")))
        except TimeoutException:
            errores.append(elementoLista)
            #print(f'error en la institucion {errores}')
            continue

            
        for ele in SegundoListaWeb:
            urlColegio=ele.get_attribute('href')
            idColegios.append(re.search(r'id=(.*?)%', urlColegio).group(1))
            
            print(idColegios)
            sleep(0.2)
            
    return idColegios,errores
    
    
    
