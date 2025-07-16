import pandas as pd

def analizar_riesgo(df):
    if df.empty or 'coeficiente' not in df.columns:
        return ["Sin datos suficientes"]

    coef = df['coeficiente']
    media = coef.mean()
    std = coef.std()

    r_inf = round(media - std, 2)
    r_sup = round(media + std, 2)
    return [f"Zona óptima: entre {r_inf}x y {r_sup}x"]