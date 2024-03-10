import pandas as pd

def GenerarExcel(Data):
    DatosColegios= pd.DataFrame(Data)
    
    print('Generando Excel')
    
    nombre_archivo = 'ejemplo.xlsx'

    #Guardar el DataFrame en un archivo XLSX
    DatosColegios.to_excel(nombre_archivo, index=False)
    