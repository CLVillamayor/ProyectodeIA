import streamlit as st

def mostrar_equipos():
    st.header("Información de los equipos")
    equipos_info = {
        "Mercedes": {
            "País": "Alemania",
            "Pilotos": ["George Russell (Inglaterra, 27 años)", "Andrea Kimi Antonelli (Italia, 18 años)"],
            "Piloto de Reserva": "Valtteri Bottas (Finlandia) y Frederik Vest (Dinamarca)",
            "Ingenieros": "Marcus Dudley (Russell), Peter Bonnington (Antonelli)",
            "Director": "Toto Wolff",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "4°",
            "Último GP": "Russell (6° largada, 5° final)"
        },
        "Red Bull Racing": {
            "País": "Austria",
            "Pilotos": ["Max Verstappen (Países Bajos, 27 años)", "Liam Lawson (Nueva Zelanda, 23 años)"],
            "Piloto de Reserva": "Yuki Tsunoda (Japón)",
            "Ingenieros": "Gianpiero Lambiase (Verstappen), Richard Wood (Lawson)",
            "Director": "Christian Horner",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "3°",
            "Último GP": "Verstappen (4° largada, 6° final), Lawson (con RB Racing) (12° largada, 17° final)"
        },
        "Ferrari": {
            "País": "Italia",
            "Pilotos": ["Charles Leclerc (Mónaco, 28 años)", "Lewis Hamilton (Inglaterra, 40 años)"],
            "Piloto de Reserva": "Antonio Giovinazzi (Italia) y Zhou Guanyu (China)",
            "Ingenieros": "Bryan Bozzi (Leclerc), Riccardo Adami (Hamilton)",
            "Director": "Frédéric Vasseur",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "2°",
            "Último GP": "Leclerc (19° largada, 3° final), Hamilton (con Mercedes)(18° largada, 4° final)"
        },
        "McLaren": {
            "País": "Reino Unido",
            "Pilotos": ["Lando Norris (Reino Unido, 25 años)", "Oscar Piastri (Australia, 23 años)"],
            "Piloto de Reserva": "Pato O'Ward (México)",
            "Ingenieros": "Will Joseph (Norris), Tom Stallard (Piastri)",
            "Director": "Adrea Stella",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "1°",
            "Último GP": "Norris (1° largada, 1° final), Piastri (2° largada, 10° final)"
        },
        "Aston Martin": {
            "País": "Reino Unido",
            "Pilotos": ["Fernando Alonso (España, 43 años)", "Lance Stroll (Canadá, 26 años)"],
            "Piloto de Reserva": "Felipe Drugovich (Brasil) y Stoffel Vandoorne (Bélgica)",
            "Ingenieros": "Andrew Vizard (Alonso), Gary Gannon (Stroll)",
            "Director": "Andy Cowell",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "5°",
            "Último GP": "Alonso (8° largada, 9° final), Stroll (13° largada, 14° final)"
        },
        "Alpine": {
            "País": "Francia",
            "Pilotos": ["Pierre Gasly (Francia, 29 años)", "Jack Doohan (Australia, 22 años)"],
            "Piloto de Reserva": "Franco Colapinto (Argentina) Ryo Hirakawa (Japón) y Paul Aron (Estonia)",
            "Ingenieros": "John Howard (Gasly), Josh Peckett (Doohan)",
            "Director": "Oliver Oakes",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "6°",
            "Último GP": "Gasly (5° largada, 7° final), Doohan (17° largada, 15° final)"
        },
        "Williams": {
            "País": "Reino Unido",
            "Pilotos": ["Alexander Albon (Tailandia, 29 años)", "Carlos Sainz Jr. (España, 31 años)"],
            "Piloto de Reserva": "Zak O'Sullivan (Reino Unido)",
            "Ingenieros": "James Urwin (Albon), Gaetan Jego (Sainz)",
            "Director": "James Vowles",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "9°",
            "Último GP": "Albon (18° largada, 11° final), Sainz (con Ferrari) (3° largada, 2° final)"
        },
        "RB": {
            "País": "Italia",
            "Pilotos": ["Yuki Tsunoda (Japón, 24 años)", "Isack Hadjar (Francia, 20 años)"],
            "Piloto de Reserva": "Ayumu Iwasa (Japón)",
            "Ingenieros": "Ernesto Desiderio (Tsunoda), Pierre Hamelin (Hadjar)",
            "Director": "Laurent Mekies",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "8°",
            "Último GP": "Tsunoda (11° largada, 12° final)"
        },
        "Sauber": {
            "País": "Suiza",
            "Pilotos": ["Nico Hulkenberg (Alemania, 37 años)", "Gabriel Bortoleto (Brasil, 20 años)"],
            "Piloto de Reserva": "Théo Pourchaire (Francia)",
            "Ingenieros": "Steven Petrik (Hulkenberg), José Manuel López (Bortoleto)",
            "Director": "Jonathan Wheatley",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "10°",
            "Último GP": "Hulkenberg (con Haas) (7° largada, 8° final)"
        },
        "Haas": {
            "País": "Estados Unidos",
            "Pilotos": ["Esteban Ocon (Francia, 28 años)", "Oliver Bearman (Reino Unido, 19 años)"],
            "Piloto de Reserva": "Pietro Fittipaldi (Brasil)",
            "Ingenieros": "Laura Mueller (Ocon), Ronan O`Hare (Bearman)",
            "Director": "Ayao Komatsu",
            "Posición en el Campeonato": "",
            "Posición en el Ultimo Campeonato": "7°",
            "Último GP": "Ocon (con Alpine/Qatar) (20° largada, 20° final)"
        }
    }

    for equipo, info in equipos_info.items():
        st.subheader(equipo)
        for key, value in info.items():
            st.write(f"{key}: {value}")