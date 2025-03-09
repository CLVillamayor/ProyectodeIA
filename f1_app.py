import streamlit as st
import equipos
import agenda
import pilotos
import guia_rapida

st.title("F1 ManijAPP")

st.write("Bienvenido a F1 ManijAPP, Tu app de Formula 1.")

# Sidebar para la navegación
st.sidebar.title("Menú")
opciones_menu = ["Inicio", "Equipos", "Agenda", "Pilotos", "Guía Rápida"]
seleccion_menu = st.sidebar.selectbox("Selecciona una sección:", opciones_menu)

# Mostrar contenido según la selección del usuario
if seleccion_menu == "Inicio":
    st.write("Selecciona una opción del menú para ver la información.")
elif seleccion_menu == "Equipos":
    equipos.mostrar_equipos()
elif seleccion_menu == "Agenda":
    agenda.mostrar_agenda()
elif seleccion_menu == "Pilotos":
    pilotos.mostrar_pilotos()
elif seleccion_menu == "Guía Rápida":
    guia_rapida.mostrar_guia_rapida()
