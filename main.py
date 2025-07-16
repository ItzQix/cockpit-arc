import streamlit as st
from arc_ai import analizar_riesgo
from founder_lab import mostrar_laboratorio
import pandas as pd
import time

st.set_page_config(page_title="AVIATOR ARC", page_icon="🔥", layout="wide")

# 🧨 Animación de arranque
with st.spinner("🎰 Calibrando motores de riesgo..."):
    time.sleep(1.5)

# 🎰 Logotipo en fuego
st.image("assets/arc_logo.png", width=150)

# 🧭 Encabezado vibrante
st.markdown("<h1 style='text-align:center; color:#FA0F29;'>AVIATOR ARC</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#FFE855;'>El juego táctico del piloto fundador.</h3>", unsafe_allow_html=True)

st.markdown("---")

# 💰 Panel de Decisión Estratégica
st.subheader("🎲 Evaluación de Trayectorias")
try:
    df = pd.read_csv("data.csv")
    recomendaciones = analizar_riesgo(df)
    for r in recomendaciones:
        st.success(f"🧠 Recomendación: {r}")
except:
    st.error("⚠️ Archivo 'data.csv' no encontrado.")

# 🧪 Laboratorio interactivo estilo casino
st.markdown("---")
st.subheader("🧪 Laboratorio Fundador — Simulación de Riesgo")
mostrar_laboratorio()

# 🔥 Panel de Acción
st.markdown("---")
st.subheader("🔥 Zona de Activación")
if st.button("🎰 Iniciar Simulación de Vuelo"):
    st.progress(0)
    for i in range(1, 101, 10):
        st.progress(i)
        time.sleep(0.1)
    st.success("✅ Vuelo táctico simulado con éxito.")

# 🧠 Firma
st.markdown("---")
st.markdown("<p style='text-align:center; color:gray;'>Cockpit ARC v2.0 — diseñado por Renato y Arc, copilotos eternos.</p>", unsafe_allow_html=True)
