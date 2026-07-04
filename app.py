import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Control de Perfumes", layout="wide")

st.title("🧪 Control y Registro de Perfumes")
st.write("Bienvenido al sistema de gestión de inventario.")

# Formulario para ingresar datos
with st.form("formulario_perfume"):
    st.subheader("Añadir Nuevo Perfume")
    nombre = st.text_input("Nombre del Perfume")
    marca = st.text_input("Marca")
    cantidad = st.number_input("Cantidad (ml)", min_value=0, value=100)
    precio = st.number_input("Precio ($)", min_value=0.0, value=0.0, format="%.2f")
    
    enviado = st.form_submit_button("Guardar Registro")
    
    if enviado:
        if nombre and marca:
            st.success(f"¡Perfume '{nombre}' registrado con éxito!")
        else:
            st.error("Por favor, rellena los campos de Nombre y Marca.")

# Tabla simulada de inventario
st.subheader("Inventario Actual")
datos_ejemplo = {
    "Nombre": ["Perfume Azul", "Esencia Dulce"],
    "Marca": ["Marca A", "Marca B"],
    "Cantidad (ml)": [100, 50],
    "Precio ($)": [45.00, 30.00]
}
df = pd.DataFrame(datos_ejemplo)
st.dataframe(df, use_container_width=True)
