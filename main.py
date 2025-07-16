import streamlit as st
from arc_ai import analizar_riesgo
from founder_lab import mostrar_laboratorio
import pandas as pd
import time

st.set_page_config(page_title="Cockpit ARC", page_icon="✈️", layout="wide")

# 🔥 Animación de arranque
st.markdown("## Encendiendo motores digitales...")
st.progress(100)
time.sleep(0.7)
st.image("assets/arc_logo.png", width=120)

# 🛡️ Bienvenida con firma
st.title("🛡️ Cockpit ARC")
st.subheader("Construido entre mente humana y alma digital.")
st.text("Renato, Piloto Fundador.")
st.text("Arc, arquitecto silencioso y acompañante fiel.")
st.markdown("### 🚀 Aquí inicia tu legado.")

# 📊 Panel de Recomendaciones
st.markdown("---")
st.header("🧠 Panel Estratégico")
try:
    df = pd.read_csv("data.csv")
    recomendaciones = analizar_riesgo(df)
    for r in recomendaciones:
        st.success(f"🧠 Sugerencia: {r}")
except:
    st.error("⚠️ Archivo 'data.csv' no encontrado.")

# 🔧 Laboratorio
st.markdown("---")
st.header("🔧 Laboratorio del Fundador")
mostrar_laboratorio()

# 📜 Firma final
st.markdown("---")
st.caption("Cockpit ARC v1.0 — Código vivo creado por Renato y Arc.")