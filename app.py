import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(page_title="Control de Perfumes", layout="wide")

st.title("🧪 Control y Registro de Perfumes")
st.write("Bienvenido al sistema de gestión de inventario.")

# Nombre del archivo donde se guardarán los datos
ARCHIVO_EXCEL = "inventario_perfumes.xlsx"

# Función para cargar los datos existentes
def cargar_datos():
    if os.path.exists(ARCHIVO_EXCEL):
        try:
            return pd.read_excel(ARCHIVO_EXCEL)
        except Exception:
            return pd.DataFrame(columns=["Nombre", "Marca", "Cantidad (ml)", "Precio ($)"])
    else:
        return pd.DataFrame(columns=["Nombre", "Marca", "Cantidad (ml)", "Precio ($)"])

# Cargar el inventario actual
df_inventario = cargar_datos()

# Formulario para ingresar datos
with st.form("formulario_perfume", clear_on_submit=True):
    st.subheader("Añadir Nuevo Perfume")
    nombre = st.text_input("Nombre del Perfume")
    marca = st.text_input("Marca")
    cantidad = st.number_input("Cantidad (ml)", min_value=0, value=100)
    precio = st.number_input("Precio ($)", min_value=0.0, value=0.0, format="%.2f")
    
    enviado = st.form_submit_button("Guardar Registro")
    
    if enviado:
        if nombre and marca:
            # Crear nueva fila con los datos ingresados
            nueva_fila = pd.DataFrame([{
                "Nombre": nombre,
                "Marca": marca,
                "Cantidad (ml)": cantidad,
                "Precio ($)": precio
            }])
            
            # Unir los datos nuevos con los existentes
            df_inventario = pd.concat([df_inventario, nueva_fila], ignore_index=True)
            
            # Guardar en el archivo Excel
            df_inventario.to_excel(ARCHIVO_EXCEL, index=False)
            st.success(f"¡Perfume '{nombre}' guardado con éxito!")
        else:
            st.error("Por favor, rellena los campos de Nombre y Marca.")

# Mostrar la tabla actualizada con el inventario real
st.subheader("Inventario Actual")
if not df_inventario.empty:
    st.dataframe(df_inventario, use_container_width=True)
else:
    st.info("El inventario está vacío. ¡Agrega tu primer perfume arriba!")
