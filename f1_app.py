import streamlit as st
import equipos
import agenda
import pilotos
import guia_rapida
import asistente

import os


# Sidebar para la navegación
st.sidebar.title("Menú")
opciones_menu = ["Inicio", "Equipos", "Agenda", "Pilotos", "Guía Rápida", "Asistente virtual Manijita"]
seleccion_menu = st.sidebar.selectbox("Selecciona una sección:", opciones_menu)

# Mostrar contenido según la selección del usuario
if seleccion_menu == "Inicio":
    st.header("Bienvenido a F1 ManijAPP , tu App sobre la Formula 1.")
    st.write("Por favor selecciona una opción del menú para ver la información.")
elif seleccion_menu == "Equipos":
    equipos.mostrar_equipos()
elif seleccion_menu == "Agenda":
    agenda.mostrar_agenda()
elif seleccion_menu == "Pilotos":
    pilotos.mostrar_pilotos()
elif seleccion_menu == "Guía Rápida":
    guia_rapida.mostrar_guia_rapida()
elif seleccion_menu == "Asistente virtual Manijita":
    asistente.main()
