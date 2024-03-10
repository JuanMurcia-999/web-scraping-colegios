
from time import sleep
from Atributos import Atributos
from GenerarExcel import GenerarExcel

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




def DatosUnicos(driver,ListaID):
    
    urlUnica='https://dueb.educacionbogota.edu.co/Dueb/cargarSede.sed?param=S&id='
    
 

    wait = WebDriverWait(driver, 5)
    
    
    Data = {
    
    "Nombre": [],
    "CodigoDANE":[], 
    "Localidad": [],
    "Direccion": [],
    "Barrio":[],
    "CodigoUPZ":[],
    "NombreUPZ":[],
    "Principal":[]
    }
    colegios= len(ListaID)
    i=1
    Jornadas=[]
    for ID in ListaID:
        
        print(F'                                                                                                                            Datos para  {i}  de {colegios}')
        driver.get(urlUnica+f'{ID}')
        for key in Data:
            Data[key].append( (wait.until(EC.presence_of_element_located((By.ID, f'{Atributos[key]}')))).get_attribute('value'))
        
           
        Peridodos=driver.find_elements(By.XPATH,"//a[contains(@href, 'cargarJornadaBySede.sed?idSede=')]")
        cantidad= len(Peridodos)
        if cantidad > 0:
            temporal=[]  
            for periodo in Peridodos:
                temporal.append(periodo.text)
                if len(temporal) == cantidad:
                    conver = '-'.join(temporal)
                    Jornadas.append(conver)
                    temporal=[]
        elif cantidad == 0:
            Jornadas.append('N/D')
        #print(Jornadas)
        i+=1    
    sleep(0.2)    
         
        
    Data['Jornada']=Jornadas   
    GenerarExcel(Data) 
    driver.quit()
    
    

