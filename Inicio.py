from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select




def Selects(driver,localidad):  
    
    wait = WebDriverWait(driver, 5)
    #Configurando selects 
    SECTOR =Select (wait.until(EC.presence_of_element_located((By.ID, 'lstColegios_prmSector_id'))))
    SECTOR.select_by_index(1)
    CLASE = Select (wait.until(EC.presence_of_element_located((By.ID, 'lstColegios_prmClaseEstablecimiento_id'))))
    CLASE.select_by_index(1) 
    LOCALIDAD = Select (wait.until(EC.presence_of_element_located((By.ID, 'lstColegios_prmLocalidad_id'))))
    LOCALIDAD.select_by_index(localidad) 

    #Click en Buscar
    BUSCAR = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@onclick=\"buscar('lstColegios')\"]"))).click()
    MOSTRAR = Select (wait.until(EC.presence_of_element_located((By.NAME, 'tipoAccionesTable_length'))))
    MOSTRAR.select_by_index(3) 
