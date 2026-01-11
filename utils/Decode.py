import numpy as np
import pandas as pd

def _norm_key(v, na_str):
    """Normaliza cualquier valor a una clave string canónica:
       - NaN/None -> na_str
       - 1.0 -> '1' ; 0.0 -> '0'
       - 1.50 -> '1.5' (sin ceros y punto sobrantes)
       - strings como ' 1.0 ' -> '1'
    """
    if pd.isna(v):
        return na_str
    # strings
    if isinstance(v, str):
        t = v.strip()
        if t == "" or t.lower() in {"nan", "none", "n/a", "na"}:
            return na_str
        # intentar numérico
        try:
            num = float(t)
            if np.isfinite(num):
                if num.is_integer():
                    return str(int(num))
                # quitar ceros/punto finales si los hay
                s = str(num).rstrip("0").rstrip(".")
                return s
        except Exception:
            # no numérico: devolver limpio
            return t
        return t
    # enteros
    if isinstance(v, (int, np.integer)):
        return str(int(v))
    # floats
    if isinstance(v, (float, np.floating)):
        if not np.isfinite(v):
            return na_str
        if float(v).is_integer():
            return str(int(v))
        s = str(v).rstrip("0").rstrip(".")
        return s
    # fallback
    return str(v)

def decoder_DF(df, code_rows, code_col, module):
    na_str = "NaN"
    # 1) Diccionario MOD_NAME -> ITM_NAME -> {CODE: DECODE} con claves normalizadas
    dict_code_rows = {}
    for (mod, itm), g in code_rows.groupby(['MOD_NAME', 'ITM_NAME'], dropna=False):
        keys   = g['CODE'].apply(lambda x: _norm_key(x, na_str))
        values = g['DECODE'].astype(str)  # los valores de decode como texto
        map_dict = dict(zip(keys, values))
        dict_code_rows.setdefault(str(mod), {})[str(itm)] = map_dict

    # 2) Aplicar mapeos del módulo solicitado; normalizando también los datos del df
    module_maps = dict_code_rows.get(module, {})
    for col in df.columns:
        if col in module_maps:
            # normalizar la serie de entrada a claves canónicas
            s_norm = df[col].apply(lambda x: _norm_key(x, na_str))
            mapped = s_norm.map(module_maps[col])
            # conservar original normalizado donde no haya mapeo
            df[col] = mapped.fillna(s_norm).astype(str)

    # 3) Renombrar columnas con code_col (ITM_NAME -> DSCR)
    code_col_map = (
        code_col.dropna(subset=['ITM_NAME', 'DSCR'])
                .drop_duplicates(subset=['ITM_NAME'], keep='first')
                .set_index('ITM_NAME')['DSCR']
                .astype(str)
                .to_dict()
    )
    df = df.rename(columns=code_col_map)

    df = df.rename(columns={'Participant ID': 'PATNO'})
    df = df.apply(lambda s: s.where(s.notna(), na_str).astype(str))
    df['PATNO'] = df['PATNO'].astype(str).str.strip()

    for col in df.columns:
        if 'NaN'in df[col].values:
            df[col].replace('NaN', np.nan, inplace=True)

    return df

    