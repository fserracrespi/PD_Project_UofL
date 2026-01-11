import pandas as pd
import os

def cols_asignacion(df, df_secundario, df_main):
    """
    Crea o actualiza un CSV con las asignaciones de columnas entre un DataFrame principal y uno secundario.

    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame del cual se obtendrán las columnas (el secundario).
    df_secundario : str
        Nombre del DataFrame secundario.
    df_main : str
        Nombre del DataFrame principal.
    ruta_csv : str, opcional
        Ruta al archivo CSV donde se guardan las asignaciones (por defecto 'asignacion.csv').
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame actualizado con todas las asignaciones.
    """
    # Crear DataFrame nuevo con las columnas actuales
    ruta_csv = '/Users/fserracrespi/Desktop/PD_Project_UofL/DATA_COLLECTION/Final_csv_files/Subject_Characteristics/asignacion_col.csv'
    nuevo = pd.DataFrame({
        'df_main': [df_main] * len(df.columns),
        'df_secundario': [df_secundario] * len(df.columns),
        'df_secundario_col': df.columns.to_list()
    })

    # Si ya existe el CSV, leerlo y concatenar
    if os.path.exists(ruta_csv):
        anterior = pd.read_csv(ruta_csv)
        combinado = pd.concat([anterior, nuevo], ignore_index=True)
    else:
        combinado = nuevo

    # Guardar el resultado actualizado
    combinado.to_csv(ruta_csv, index=False, encoding='utf-8-sig')

    return combinado
 
def cols_asignacion2(df, df_secundario, df_main):
    """
    Crea o actualiza un CSV con las asignaciones de columnas entre un DataFrame principal y uno secundario.

    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame del cual se obtendrán las columnas (el secundario).
    df_secundario : str
        Nombre del DataFrame secundario.
    df_main : str
        Nombre del DataFrame principal.
    ruta_csv : str, opcional
        Ruta al archivo CSV donde se guardan las asignaciones (por defecto 'asignacion.csv').
    
    Retorna:
    --------
    pd.DataFrame
        DataFrame actualizado con todas las asignaciones.
    """
    # Crear DataFrame nuevo con las columnas actuales
    ruta_csv = '/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PD_CSV_CLEAN/FINAL DATA TEST CLEAN/FINAL_ASSIGNATION_COL.csv'
    nuevo = pd.DataFrame({
        'df_main': [df_main] * len(df.columns),
        'df_secundario': [df_secundario] * len(df.columns),
        'df_secundario_col': df.columns.to_list()
    })

    # Si ya existe el CSV, leerlo y concatenar
    if os.path.exists(ruta_csv):
        anterior = pd.read_csv(ruta_csv)
        combinado = pd.concat([anterior, nuevo], ignore_index=True)
    else:
        combinado = nuevo

    # Guardar el resultado actualizado
    combinado.to_csv(ruta_csv, index=False, encoding='utf-8-sig')

    return combinado
 