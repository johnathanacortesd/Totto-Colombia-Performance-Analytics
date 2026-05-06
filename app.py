import streamlit as st
import streamlit.components.v1 as components

# Configuración de la página para que ocupe todo el ancho
st.set_page_config(page_title="Dashboard Performance Totto", layout="wide")

# Ocultar el menú por defecto de Streamlit para que parezca una web propia
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# ---------------------------------------------------------
# SISTEMA BÁSICO DE PROTECCIÓN POR CONTRASEÑA
# ---------------------------------------------------------
def check_password():
    """Devuelve True si la contraseña es correcta."""
    def password_entered():
        # Aquí defines la contraseña que le darás a tu cliente
        if st.session_state["password"] == "totto2026":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Borrar por seguridad
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input("🔒 Ingrese la contraseña para ver el dashboard", type="password", on_change=password_entered, key="password")
        return False
    elif not st.session_state["password_correct"]:
        st.text_input("🔒 Ingrese la contraseña para ver el dashboard", type="password", on_change=password_entered, key="password")
        st.error("Contraseña incorrecta")
        return False
    return True

# ---------------------------------------------------------
# RENDERIZADO DEL DASHBOARD
# ---------------------------------------------------------
if check_password():
    # Leer el archivo HTML
    with open("dashboard_campanas_colombia.html", "r", encoding="utf-8") as f:
        html_data = f.read()
    
    # TIP PRO PARA TIEMPO REAL: 
    # Aquí en el futuro puedes hacer llamadas a bases de datos con Python 
    # y usar html_data.replace('DATOS_AQUI', datos_de_python) antes de renderizar.
    
    # Renderizar el HTML en la aplicación con altura suficiente para evitar doble scroll
    components.html(html_data, height=2400, scrolling=True)
