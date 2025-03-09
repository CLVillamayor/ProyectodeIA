import streamlit as st

def mostrar_agenda():
    st.header("Información de las carreras")
    carreras_info = {
        "GP de Australia": {
            "fecha": "14-16 de marzo",
            "circuito": "Circuito de Albert Park",
            "longitud": "5.303 km",
            "vueltas": 58,
            "Horarios de Carrera": "ARG:01:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de China": {
            "fecha": "21-23 de marzo",
            "circuito": "Circuito Internacional de Shanghái",
            "longitud": "5.451 km",
            "vueltas": 56,
            "Horarios de Carrera": "ARG:00:00HS Y 04:00HS ",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Japón": {
            "fecha": "4-6 de abril",
            "circuito": "Circuito de Suzuka",
            "longitud": "5.807 km",
            "vueltas": 53,
            "Horarios de Carrera": "ARG:02:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Baréin": {
            "fecha": "11-13 de abril",
            "circuito": "Circuito Internacional de Baréin",
            "longitud": "5.412 km",
            "vueltas": 57,
            "Horarios de Carrera": "ARG:12:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Arabia Saudita": {
            "fecha": "18-20 de abril",
            "circuito": "Circuito Corniche de Yeda",
            "longitud": "6.174 km",
            "vueltas": 50,
            "Horarios de Carrera": "ARG:14:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Miami": {
            "fecha": "2-4 de mayo",
            "circuito": "Autódromo Internacional de Miami",
            "longitud": "5.412 km",
            "vueltas": 57,
            "Horarios de Carrera": "ARG:13:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Emilia-Romaña": {
            "fecha": "16-18 de mayo",
            "circuito": "Autódromo Enzo e Dino Ferrari",
            "longitud": "4.909 km",
            "vueltas": 63,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Mónaco": {
            "fecha": "23-25 de mayo",
            "circuito": "Circuito de Mónaco",
            "longitud": "3.337 km",
            "vueltas": 78,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de España": {
            "fecha": "30 de mayo - 1 de junio",
            "circuito": "Circuito de Barcelona-Cataluña",
            "longitud": "4.675 km",
            "vueltas": 66,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Canadá": {
            "fecha": "13-15 de junio",
            "circuito": "Circuito Gilles Villeneuve",
            "longitud": "4.361 km",
            "vueltas": 70,
            "Horarios de Carrera": "ARG:15:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Austria": {
            "fecha": "27-29 de junio",
            "circuito": "Red Bull Ring",
            "longitud": "4.318 km",
            "vueltas": 71,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Gran Bretaña": {
            "fecha": "4-6 de julio",
            "circuito": "Circuito de Silverstone",
            "longitud": "5.891 km",
            "vueltas": 52,
            "Horarios de Carrera": "ARG:11:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Bélgica": {
            "fecha": "25-27 de julio",
            "circuito": "Circuito de Spa-Francorchamps",
            "longitud": "7.004 km",
            "vueltas": 44,
            "Horarios de Carrera": "ARG:07:00HS Y 10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Hungría": {
            "fecha": "1-3 de agosto",
            "circuito": "Hungaroring",
            "longitud": "4.381 km",
            "vueltas": 70,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Países Bajos": {
            "fecha": "29-31 de agosto",
            "circuito": "Circuito de Zandvoort",
            "longitud": "4.259 km",
            "vueltas": 72,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Italia": {
            "fecha": "5-7 de septiembre",
            "circuito": "Autódromo Nacional de Monza",
            "longitud": "5.793 km",
            "vueltas": 53,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Azerbaiyán": {
            "fecha": "19-21 de septiembre",
            "circuito": "Circuito callejero de Bakú",
            "longitud": "6.003 km",
            "vueltas": 51,
            "Horarios de Carrera": "ARG:08:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Singapur": {
            "fecha": "3-5 de octubre",
            "circuito": "Circuito callejero de Marina Bay",
            "longitud": "5.063 km",
            "vueltas": 61,
            "Horarios de Carrera": "ARG:09:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Estados Unidos": {
            "fecha": "17-19 de octubre",
            "circuito": "Circuito de las Américas",
            "longitud": "5.513 km",
            "vueltas": 56,
            "Horarios de Carrera": "ARG:14:00HS Y 16:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de México": {
            "fecha": "24-26 de octubre",
            "circuito": "Autódromo Hermanos Rodríguez",
            "longitud": "4.304 km",
            "vueltas": 71,
            "Horarios de Carrera": "ARG:17:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Brasil": {
            "fecha": "7-9 de noviembre",
            "circuito": "Autódromo José Carlos Pace",
            "longitud": "4.309 km",
            "vueltas": 71,
            "Horarios de Carrera": "ARG:11:00HS Y 14:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Las Vegas": {
            "fecha": "20-22 de noviembre",
            "circuito": "Circuito callejero de Las Vegas",
            "longitud": "6.201 km",
            "vueltas": 50,
            "Horarios de Carrera": "ARG:01:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Catar": {
            "fecha": "28-30 de noviembre",
            "circuito": "Circuito Internacional de Lusail",
            "longitud": "5.419 km",
            "vueltas": 57,
            "Horarios de Carrera": "ARG:11:00HS Y 13:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
        "GP de Abu Dabi": {
            "fecha": "5-7 de diciembre",
            "circuito": "Circuito de Yas Marina",
            "longitud": "5.281 km",
            "vueltas": 58,
            "Horarios de Carrera": "ARG:10:00HS",
            "Televisacion en Arg": "F1 TV, Disney+ ,Fox Sports, AlanguloTV.com"},
    }

    for carrera, info in carreras_info.items():
        st.subheader(carrera)
        for key, value in info.items():
            st.write(f"{key}: {value}")