import streamlit as st

def mostrar_pilotos():
    st.header("Sección de pilotos de la temporada de Formula 1")
    st.write("Por favor, elije un piloto.")

    pilotos_info = {
        "Lando Norris": {
            "Fecha de nacimiento": "13 de noviembre de 1999",
            "Edad actual": "25 años",
            "Nacionalidad": "Británico",
            "Equipo actual": "McLaren Formula 1 Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "McLaren (2019)"
        },
        "Oscar Piastri": {
            "Fecha de nacimiento": "6 de abril de 2001",
            "Edad actual": "23 años",
            "Nacionalidad": "Australiano",
            "Equipo actual": "McLaren Formula 1 Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "McLaren (2023)"
        },
        "Charles Leclerc": {
            "Fecha de nacimiento": "16 de octubre de 1997",
            "Edad actual": "27 años",
            "Nacionalidad": "Monegasco",
            "Equipo actual": "Scuderia Ferrari HP",
            "Rol": "Titular",
            "Equipo de debut en F1": "Sauber (2018)"
        },
        "Lewis Hamilton": {
            "Fecha de nacimiento": "7 de enero de 1985",
            "Edad actual": "40 años",
            "Nacionalidad": "Británico",
            "Equipo actual": "Scuderia Ferrari HP",
            "Rol": "Titular",
            "Equipo de debut en F1": "McLaren (2007)"
        },
        "Max Verstappen": {
            "Fecha de nacimiento": "30 de septiembre de 1997",
            "Edad actual": "27 años",
            "Nacionalidad": "Neerlandés",
            "Equipo actual": "Oracle Red Bull Racing",
            "Rol": "Titular",
            "Equipo de debut en F1": "Toro Rosso (2015)"
        },
        "Liam Lawson": {
            "Fecha de nacimiento": "11 de febrero de 2002",
            "Edad actual": "23 años",
            "Nacionalidad": "Neozelandés",
            "Equipo actual": "Oracle Red Bull Racing",
            "Rol": "Titular",
            "Equipo de debut en F1": "Racing Bulls (2024)"
        },
        "George Russell": {
            "Fecha de nacimiento": "15 de febrero de 1998",
            "Edad actual": "27 años",
            "Nacionalidad": "Británico",
            "Equipo actual": "Mercedes-AMG Petronas Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "Williams (2019)"
        },
        "Andrea Kimi Antonelli": {
            "Fecha de nacimiento": "25 de agosto de 2006",
            "Edad actual": "18 años",
            "Nacionalidad": "Italiano",
            "Equipo actual": "Mercedes-AMG Petronas Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "2025"
        },
        "Fernando Alonso": {
            "Fecha de nacimiento": "29 de julio de 1981",
            "Edad actual": "43 años",
            "Nacionalidad": "Español",
            "Equipo actual": "Aston Martin Aramco Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "Minardi (2001)"
        },
        "Lance Stroll": {
            "Fecha de nacimiento": "29 de octubre de 1998",
            "Edad actual": "26 años",
            "Nacionalidad": "Canadiense",
            "Equipo actual": "Aston Martin Aramco Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "Williams (2017)"
        },
        "Jack Doohan": {
            "Fecha de nacimiento": "20 de enero de 2003",
            "Edad actual": "22 años",
            "Nacionalidad": "Australiano",
            "Equipo actual": "BWT Alpine Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "BWT Alpine Formula One Team (2024)"
        },
        "Pierre Gasly": {
            "Fecha de nacimiento": "7 de febrero de 1996",
            "Edad actual": "29 años",
            "Nacionalidad": "Francés",
            "Equipo actual": "BWT Alpine Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "Toro Rosso (2017)"
        },
        "Esteban Ocon": {
            "Fecha de nacimiento": "17 de septiembre de 1996",
            "Edad actual": "28 años",
            "Nacionalidad": "Francés",
            "Equipo actual": "MoneyGram Haas F1 Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "Manor (2016)"
        },
        "Oliver Bearman": {
            "Fecha de nacimiento": "8 de mayo de 2005",
            "Edad actual": "19 años",
            "Nacionalidad": "Británico",
            "Equipo actual": "Haas F1 Team",
            "Rol": "Piloto titular",
            "Equipo de debut en F1": "Scuderia Ferrari (2024)"
        },
        "Isack Hadjar": {
            "Fecha de nacimiento": "28 de septiembre de 2004",
            "Edad actual": "20 años",
            "Nacionalidad": "Francés",
            "Equipo actual": "Visa Cash App Racing Bulls Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "2025"
        },
        "Yuki Tsunoda": {
            "Fecha de nacimiento": "11 de mayo de 2000",
            "Edad actual": "24 años",
            "Nacionalidad": "Japonés",
            "Equipo actual": "Visa Cash App Racing Bulls Formula One Team",
            "Rol": "Titular",
            "Equipo de debut en F1": "AlphaTauri (2021)"
        },
        "Franco Colapinto": {
            "Fecha de nacimiento": "27 de mayo de 2003",
            "Edad actual": "21 años",
            "Nacionalidad": "Argentino",
            "Equipo actual": "BWT Alpine Formula One Team",
            "Rol": "Piloto de reserva",
            "Equipo de debut en F1": "Williams Racing (2024)"
        },
        "Valtteri Bottas": {
            "Fecha de nacimiento": "28 de agosto de 1989",
            "Edad actual": "35 años",
            "Nacionalidad": "Finlandés",
            "Equipo actual": "Mercedes-AMG Petronas Formula One Team",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Williams (2013)"
        },
        "Zhou Guanyu": {
            "Fecha de nacimiento": "30 de mayo de 1999",
            "Edad actual": "25 años",
            "Nacionalidad": "Chino",
            "Equipo actual": "Scuderia Ferrari HP",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Alfa Romeo (2022)"
        },
        "Antonio Giovinazzi": {
            "Fecha de nacimiento": "14 de diciembre de 1993",
            "Edad actual": "31 años",
            "Nacionalidad": "Italiano",
            "Equipo actual": "Scuderia Ferrari HP",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Sauber (2017)"
        },
        "Paul Aron": {
            "Fecha de nacimiento": "4 de febrero de 2004",
            "Edad actual": "21 años",
            "Nacionalidad": "Estonio",
            "Equipo actual": "BWT Alpine Formula One Team",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Aún no ha debutado"
        },
        "Ryō Hirakawa": {
            "Fecha de nacimiento": "7 de marzo de 1994",
            "Edad actual": "31 años",
            "Nacionalidad": "Japonés",
            "Equipo actual": "BWT Alpine Formula One Team",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Aún no ha debutado"
        },
        "Felipe Drugovich": {
            "Fecha de nacimiento": "23 de mayo de 2000",
            "Edad actual": "24 años",
            "Nacionalidad": "Brasileño",
            "Equipo actual": "Aston Martin Aramco Formula One Team",
            "Rol": "Piloto de reserva",
            "Equipo de debut en F1": "Aún no ha debutado"
        },
        "Stoffel Vandoorne": {
            "Fecha de nacimiento": "26 de marzo de 1992",
            "Edad actual": "33 años",
            "Nacionalidad": "Belga",
            "Equipo actual": "Aston Martin Aramco Formula One Team",
            "Rol": "Reserva",
            "Equipo de debut en F1": "McLaren (2016)"
        },
        "Ayumu Iwasa": {
            "Fecha de nacimiento": "22 de septiembre de 2001",
            "Edad actual": "23 años",
            "Nacionalidad": "Japonés",
            "Equipo actual": "Visa Cash App Racing Bulls Formula One Team",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Aún no ha debutado"
        },
        "Oliver Turvey": {
            "Fecha de nacimiento": "1 de abril de 1987",
            "Edad actual": "37 años",
            "Nacionalidad": "Británico",
            "Equipo actual": "Atlassian Williams Racing",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Aún no ha debutado"
        },
        "Arthur Leclerc": {
            "Fecha de nacimiento": "14 de octubre de 2000",
            "Edad actual": "24 años",
            "Nacionalidad": "Monegasco",
            "Equipo actual": "Scuderia Ferrari HP",
            "Rol": "Reserva",
            "Equipo de debut en F1": "Aún no ha debutado"
        }
    }

    opciones_pilotos = list(pilotos_info.keys())
    seleccion_piloto = st.selectbox("Selecciona un piloto:", opciones_pilotos)

    if seleccion_piloto:
        st.header(seleccion_piloto)
        for key, value in pilotos_info[seleccion_piloto].items():
            st.write(f"{key}: {value}")