import streamlit as st

def mostrar_laboratorio():
    st.subheader("⚙️ Simulador de Trayectorias")
    vel = st.slider("Velocidad (x)", 1.0, 3.0, 1.5)
    riesgo = st.selectbox("Riesgo", ["Bajo", "Medio", "Alto"])
    estab = st.slider("Estabilidad (%)", 0, 100, 75)

    st.markdown("---")
    st.success(f"📡 Parámetros:")
    st.write(f"Velocidad: {vel}x")
    st.write(f"Riesgo: {riesgo}")
    st.write(f"Estabilidad: {estab}%")

    if vel > 2.5 and riesgo == "Alto":
        st.error("⚠️ Riesgo extremo. Revisa estrategia.")
    elif estab < 40:
        st.warning("🌀 Sistema inestable.")
    else:
        st.info("✅ Trayectoria viable.")