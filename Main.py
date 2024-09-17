from Abrir import Abrir
from DatosColegio import DatosUnicos
from primeralista import PrimerLista
from GenerarExcel import GenerarExcel 
from IDcolegiosUnicos import colegiosUnicos
from Atributos import AtributosColegios

Localidades = list(range(2,22))
driver = Abrir()


IdsBuenos,IdsMalos = PrimerLista(driver,Localidades)
print('/////////////////////////////Data Buenos///////////////////////////////////////////////')
Data1=DatosUnicos(driver, IdsBuenos)
#GenerarExcel(DataBuenos)
print('/////////////////////////////Data Malos////////////////////////////////////////////////')
Data2=colegiosUnicos(driver,IdsMalos)


Data_unificado = {}

# Agregar los elementos de Data1 al diccionario unificado
for key, value in Data1.items():
    if key in Data2:
        Data_unificado[key] = value + Data2[key]
    else:
        Data_unificado[key] = value

# Agregar los elementos de Data2 que no están en Data1 al diccionario unificado
for key, value in Data2.items():
        if key not in Data_unificado:
            Data_unificado[key] = value
        
        
for key, value in Data_unificado.items():
    print(f'{key}{len(value)}')
GenerarExcel(Data_unificado)