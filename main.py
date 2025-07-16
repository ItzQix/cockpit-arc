import streamlit as st

st.set_page_config(page_title="Aviator ARC", page_icon="✈️", layout="centered")

# 🛫 Título principal
st.title("✈️ Aviator ARC")
st.markdown("#### Predicción y juego táctico para multiplicadores de vuelo")

# 🎮 Zona de entrada inicial
st.markdown("---")
st.subheader("🎲 Apuesta tu monto")
apuesta = st.number_input("Ingresa tu apuesta ($)", min_value=0.0, format="%.2f")

# 🚨 Zona de acción básica
st.markdown("---")
st.subheader("🚀 Simulador básico del avión (v1)")
distancia = st.slider("Distancia que el avión recorrió (multiplicador)", 1.0, 10.0, 1.5, 0.1)

# 🪂 Botón de salto
if st.button("🪂 Saltar del avión"):
    resultado = round(apuesta * distancia, 2)
    st.success(f"¡Saltaste a tiempo! 🛡️ Ganaste ${resultado}")
else:
    st.warning("🛬 No has saltado aún. El avión sigue volando...")

# 🧠 Pie de firma
st.markdown("---")
st.caption("Cockpit ARC — Simulador de apuestas tácticas ✈️ creado por Renato & Arc")
