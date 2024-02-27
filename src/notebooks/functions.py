import pandas as pd

def prettyColumNames(df):
    '''
    Cambia los nombres de las columnas en el dataframe df a minúsculas y reemplazar los espacios en
    blanco por guiones bajos ('_')
    '''
    # Obtener los nombres de las columnas actuales
    nombresColumnas = df.columns.tolist()
    
    # Crear un diccionario para mapear los nombres de las columnas
    mapeoNombres = {nombre: nombre.upper().replace(' ', '_') for nombre in nombresColumnas}
    
    # Renombrar las columnas utilizando el diccionario de mapeo
    df.rename(columns = mapeoNombres, inplace = True)
    
    # Retornar el dataframe con los nombres de las columnas modificados
    return df.columns