import numpy as np
import pandas as pd



def check_progression(df, name_prefix="SUBJECT"):
    """
    Genera un DataFrame donde cada columna representa una combinación específica
    de progression (ej. SUBJECT_Prog_1y_(BL+V04)) indicando si el PATNO cumple esa secuencia.
    """

    progressions = {
        "Prog_1y": [["BL", "V04"], ["V04", "V06"], ["V06", "V08"], ["V08", "V10"], ["V10", "V12"]],
        "Prog_2y": [["BL", "V04", "V06"], ["V04", "V06", "V08"], ["V06", "V08", "V10"], ["V08", "V10", "V12"]],
        "Prog_3y": [["BL", "V04", "V06", "V08"], ["V04", "V06", "V08", "V10"], ["V06", "V08", "V10", "V12"]],
        "Prog_4y": [["BL", "V04", "V06", "V08", "V10"], ["V04", "V06", "V08", "V10", "V12"]],
        "Prog_5y": [["BL", "V04", "V06", "V08", "V10", "V12"]],
    }

    records = []

    for patno, group in df.groupby('PATNO'):
        visits = set(group['Visit ID'])

        for prog_name, combos in progressions.items():
            for combo in combos:
                # Construir nombre de columna en formato (BL+V04+V06)
                combo_str = "+".join(combo)
                col_name = f"{name_prefix}_{prog_name}_({combo_str})"

                eligible = set(combo).issubset(visits)
                records.append({
                    'PATNO': patno,
                    'Progression': col_name,
                    'Eligible': eligible
                })

    # Crear DataFrame largo
    progression_long = pd.DataFrame(records)

    # Pivotar a formato ancho
    progression_wide = progression_long.pivot(
        index='PATNO', columns='Progression', values='Eligible'
    ).fillna(False)

    # Ordenar columnas
    progression_wide = progression_wide.reindex(sorted(progression_wide.columns), axis=1)

    return progression_wide


def progression_csv_upgrade(df,prefix="None"):

    df = check_progression(df, name_prefix=prefix)
    df.reset_index(inplace=True)

    p1 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(BL+V04)_12SEP2025.csv', dtype=str)
    p1 = p1.merge(df[df.columns[[0,1]]], on='PATNO', how='left')
    p1.fillna(False, inplace=True)
    p1.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(BL+V04)_12SEP2025.csv', index=False)
    

    p2 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V04+V06)_12SEP2025.csv', dtype=str)
    p2 = p2.merge(df[df.columns[[0,2]]], on='PATNO', how='left')
    p2.fillna(False, inplace=True)
    p2.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V04+V06)_12SEP2025.csv', index=False)
    

    p3 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V06+V08)_12SEP2025.csv', dtype=str)
    p3 = p3.merge(df[df.columns[[0,3]]], on='PATNO', how='left')
    p3.fillna(False, inplace=True)
    p3.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V06+V08)_12SEP2025.csv', index=False)
    

    p4 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V08+V10)_12SEP2025.csv', dtype=str)
    p4 = p4.merge(df[df.columns[[0,4]]], on='PATNO', how='left')
    p4.fillna(False, inplace=True)
    p4.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V08+V10)_12SEP2025.csv', index=False)
    

    p5 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V10+V12)_12SEP2025.csv', dtype=str)
    p5 = p5.merge(df[df.columns[[0,5]]], on='PATNO', how='left')
    p5.fillna(False, inplace=True)
    p5.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_1y_(V10+V12)_12SEP2025.csv', index=False)
    
    p6 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(BL+V04+V06)_12SEP2025.csv', dtype=str)
    p6 = p6.merge(df[df.columns[[0,6]]], on='PATNO', how='left')
    p6.fillna(False, inplace=True)
    p6.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(BL+V04+V06)_12SEP2025.csv', index=False)
    

    p7 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(V04+V06+V08)_12SEP2025.csv', dtype=str)
    p7 = p7.merge(df[df.columns[[0,7]]], on='PATNO', how='left')
    p7.fillna(False, inplace=True)
    p7.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(V04+V06+V08)_12SEP2025.csv', index=False)  
    

    p8 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(V06+V08+V10)_12SEP2025.csv', dtype=str)
    p8 = p8.merge(df[df.columns[[0,8]]], on='PATNO', how='left')
    p8.fillna(False, inplace=True)
    p8.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(V06+V08+V10)_12SEP2025.csv', index=False)
    
    p9 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(V08+V10+V12)_12SEP2025.csv', dtype=str)
    p9 = p9.merge(df[df.columns[[0,9]]], on='PATNO', how='left')
    p9.fillna(False, inplace=True)
    p9.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_2y_(V08+V10+V12)_12SEP2025.csv', index=False)
    

    p10 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_3y_(BL+V04+V06+V08)_12SEP2025.csv', dtype=str)
    p10 = p10.merge(df[df.columns[[0,10]]], on='PATNO', how='left')
    p10.fillna(False, inplace=True)
    p10.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_3y_(BL+V04+V06+V08)_12SEP2025.csv', index=False)
    

    p11 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_3y_(V04+V06+V08+V10)_12SEP2025.csv', dtype=str)
    p11 = p11.merge(df[df.columns[[0,11]]], on='PATNO', how='left')
    p11.fillna(False, inplace=True)
    p11.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_3y_(V04+V06+V08+V10)_12SEP2025.csv', index=False)
    

    p12 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_3y_(V06+V08+V10+V12)_12SEP2025.csv', dtype=str)
    p12 = p12.merge(df[df.columns[[0,12]]], on='PATNO', how='left')
    p12.fillna(False, inplace=True)
    p12.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_3y_(V06+V08+V10+V12)_12SEP2025.csv', index=False)
    

    p13 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_4y_(BL+V04+V06+V08+V10)_12SEP2025.csv', dtype=str)
    p13 = p13.merge(df[df.columns[[0,13]]], on='PATNO', how='left')
    p13.fillna(False, inplace=True)
    p13.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_4y_(BL+V04+V06+V08+V10)_12SEP2025.csv', index=False)
    

    p14 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_4y_(V04+V06+V08+V10+V12)_12SEP2025.csv', dtype=str)
    p14 = p14.merge(df[df.columns[[0,14]]], on='PATNO', how='left')
    p14.fillna(False, inplace=True)
    p14.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_4y_(V04+V06+V08+V10+V12)_12SEP2025.csv', index=False)
    
    p15 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_5y_(BL+V04+V06+V08+V10+V12)_12SEP2025.csv', dtype=str)
    p15 = p15.merge(df[df.columns[[0,15]]], on='PATNO', how='left')
    p15.fillna(False, inplace=True)
    p15.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/SUBJECT_Prog_5y_(BL+V04+V06+V08+V10+V12)_12SEP2025.csv', index=False)
    

    return print("Progression CSV files updated successfully.")




def check_progression_multi(df, name_prefix=""):

    progressions = {
        "Prog_1y": [["BL", "V04"], ["V04", "V06"], ["V06", "V08"], ["V08", "V10"], ["V10", "V12"]],
        "Prog_2y": [["BL", "V04", "V06"], ["V04", "V06", "V08"], ["V06", "V08", "V10"], ["V08", "V10", "V12"]],
        "Prog_3y": [["BL", "V04", "V06", "V08"], ["V04", "V06", "V08", "V10"], ["V06", "V08", "V10", "V12"]],
        "Prog_4y": [["BL", "V04", "V06", "V08", "V10"], ["V04", "V06", "V08", "V10", "V12"]],
        "Prog_5y": [["BL", "V04", "V06", "V08", "V10", "V12"]],
    }

    # Crear lista vacía para resultados
    records = []

    # Agrupar por paciente
    for patno, group in df.groupby('PATNO'):
        visits = set(group['Visit ID'])
        for prog_name, combos in progressions.items():
            eligible = any(set(combo).issubset(visits) for combo in combos)
            records.append({
                'PATNO': patno,
                'Progression': prog_name,
                'Eligible': eligible
            })

    # Crear DataFrame limpio
    progression_long = pd.DataFrame(records)

    # Pasar a formato ancho
    progression_wide = progression_long.pivot(index='PATNO', columns='Progression', values='Eligible').fillna(False)

    # Añadir prefijo si se proporciona
    if name_prefix:
        progression_wide.columns = [f"{name_prefix}_{col}" for col in progression_wide.columns]

    return progression_wide


def progression_multi_csv_upgrade(df,prefix="None"):

    df = check_progression_multi(df, name_prefix=prefix)
    df.reset_index(inplace=True)

    p1 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_1y12SEP2025.csv', dtype=str)
    p1 = p1.merge(df[df.columns[[0,1]]], on='PATNO', how='left')
    p1.fillna(False, inplace=True)
    p1.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_1y12SEP2025.csv', index=False)
    

    p2 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_2y12SEP2025.csv', dtype=str)
    p2 = p2.merge(df[df.columns[[0,2]]], on='PATNO', how='left')
    p2.fillna(False, inplace=True)
    p2.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_2y12SEP2025.csv', index=False)
    

    p3 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_3y12SEP2025.csv', dtype=str)
    p3 = p3.merge(df[df.columns[[0,3]]], on='PATNO', how='left')
    p3.fillna(False, inplace=True)
    p3.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_3y12SEP2025.csv', index=False)
    

    p4 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_4y12SEP2025.csv', dtype=str)
    p4 = p4.merge(df[df.columns[[0,4]]], on='PATNO', how='left')
    p4.fillna(False, inplace=True)
    p4.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_4y12SEP2025.csv', index=False)
    

    p5 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_5y12SEP2025.csv', dtype=str)
    p5 = p5.merge(df[df.columns[[0,5]]], on='PATNO', how='left')
    p5.fillna(False, inplace=True)
    p5.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/MULTIPLE_SUBJECT_Prog_5y12SEP2025.csv', index=False)
    

    return print("MULTI Progression CSV files updated successfully.")



def check_visits(df, name_prefix=""):
    # Lista de visitas que te interesan
    visits = ["BL", "V04", "V06", "V08", "V10", "V12"]
    
    records = []

    # Agrupar por paciente
    for patno, group in df.groupby('PATNO'):
        patient_visits = set(group['Visit ID'])
        record = {'PATNO': patno}
        for visit in visits:
            record[visit] = visit in patient_visits
        records.append(record)

    # Crear DataFrame final
    visit_wide = pd.DataFrame(records)

    # Añadir prefijo si se especifica
    if name_prefix:
        visit_wide = visit_wide.rename(columns={v: f"{name_prefix}_{v}" for v in visits})

    return visit_wide

def visit_csv_upgrade(df, prefix=""):

    df = check_visits(df, name_prefix=prefix)
    
    pBL = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_BL_12SEP2025.csv', dtype=str)
    pBL = pBL.merge(df[df.columns[[0,1]]], on='PATNO', how='left')
    pBL.fillna(False, inplace=True)
    pBL.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_BL_12SEP2025.csv', index=False)
    

    pV04 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V04_12SEP2025.csv', dtype=str)
    pV04 = pV04.merge(df[df.columns[[0,2]]], on='PATNO', how='left')
    pV04.fillna(False, inplace=True)
    pV04.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V04_12SEP2025.csv', index=False)
    
    pV06 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V06_12SEP2025.csv', dtype=str)
    pV06 = pV06.merge(df[df.columns[[0,3]]], on='PATNO', how='left')
    pV06.fillna(False, inplace=True)
    pV06.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V06_12SEP2025.csv', index=False)
    

    pV08 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V08_12SEP2025.csv', dtype=str)
    pV08 = pV08.merge(df[df.columns[[0,4]]], on='PATNO', how='left')
    pV08.fillna(False, inplace=True)
    pV08.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V08_12SEP2025.csv', index=False)
    

    pV10 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V10_12SEP2025.csv', dtype=str)
    pV10 = pV10.merge(df[df.columns[[0,5]]], on='PATNO', how='left')
    pV10.fillna(False, inplace=True)
    pV10.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V10_12SEP2025.csv', index=False)
    

    pV12 = pd.read_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V12_12SEP2025.csv', dtype=str)
    pV12 = pV12.merge(df[df.columns[[0,6]]], on='PATNO', how='left')
    pV12.fillna(False, inplace=True)
    pV12.to_csv('/Users/fserracrespi/Desktop/PD_Project_UofL/PD_DATA/PROGRESSION_STUDIES/VISITS_SUBJECT_V12_12SEP2025.csv', index=False)
    return print("Visits CSV files updated successfully.")