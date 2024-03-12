import re
import itertools
from time import sleep
from Atributos import AtributosColegios
from GenerarExcel import GenerarExcel

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def colegiosUnicos(driver,malos):
    #malos =  list(itertools.chain(*listmalos))
    wait = WebDriverWait(driver, 5)
    colegios=len(malos)
    
    Data = {
    
    "Nombre": [],
    "CodigoDANE":[], 
    "Localidad": [],
    "Direccion": [],
    "Barrio":[],
    "CodigoUPZ":[],
    "NombreUPZ":[],
    "Principal":[],
    "Jornadas":[],
    "Numsede":[]
    }
    i=1
    for url in malos:
        
        print(F'                                                                                                                            Datos para  {i}  de {colegios} ')
        driver.get(url)
        for key in Data:
            
            if key == 'Principal':
                Data[key].append('SI')
            elif key =='Nombre':
                NombreCompleto=wait.until(EC.presence_of_element_located((By.XPATH,"(//strong)[1]"))).text
                Data[key].append(re.search(r'ESTABLECIMIENTO EDUCATIVO:(.*?)\(', NombreCompleto).group(1))
            elif key == "Numsede":
                Data[key].append('S1')
            elif key =='Jornadas':
                temporal=[]
                lis=wait.until(EC.presence_of_all_elements_located((By.XPATH,"(//ol)[4]//li")))
                count=len(lis)
                if count > 0:
                    for li in lis:
                        
                        temporal.append(li.text)
                        print(temporal)
                        if len(temporal) == count:
                            conver = '-'.join(temporal)
                            print(conver)
                            Data[key].append(conver)
                            temporal=[]  
                else:
                      Data[key].append('N/D')                                
            else: 
                Data[key].append( (wait.until(EC.presence_of_element_located((By.ID, f'{AtributosColegios[key]}')))).get_attribute('value'))
                
      
        i+=1 
    print(Data["Jornadas"])   
    sleep(0.2)
    driver.quit()
    return Data  