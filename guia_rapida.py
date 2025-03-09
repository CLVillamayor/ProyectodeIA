import streamlit as st

def mostrar_guia_rapida():
    st.header("Guía Rápida")

    opciones_guia = [
        "La Parrilla",
        "Los Monoplazas",
        "El Fin de Semana",
        "Gran Premio",
        "Puntos por Posición",
        "Cambio de Neumáticos",
        "Banderas",
        "Techo Presupuestario"]
    seleccion = st.selectbox("Selecciona una opción:", opciones_guia)

    if seleccion == "La Parrilla":
        st.write("La actual parrilla de Formula 1 está conformada por 10 equipos de dos autos cada uno. Los monoplazas son distintos entre ellos debido al desarrollo de cada escudería, pero con lineamientos rígidos por parte de la categoría, como el motor V6 híbrido, la altura, el largo en la distancia de los ejes y las medidas de seguridad, por ejemplo.")
    elif seleccion == "Los Monoplazas":
        st.write("Los siguientes constructores y pilotos están actualmente bajo contrato para competir en el Campeonato Mundial de 2025. Todos los equipos competirán con neumáticos suministrados por la empresa Pirelli:")
        st.write("Escuderia: McLaren Formula 1 Team. Chasis: McLaren MCL39 Motor: Mercedes-AMG F1 M16 Pilotos:  4-Lando Norris	NOR.  81- Oscar Piastri PIA.")
        st.write("Escuderia: Scuderia Ferrari HP. Chasis:Ferrari SF-25 Motor: Ferrari 066/12 Pilotos: 16-Charles Leclerc LEC. 44-Lewis Hamilton HAM.")
        st.write("Escuderia: Oracle Red Bull Racing Chasis: Red Bull RB21 Motor: Honda RBPTH002 Pilotos:1-Max Verstappen VER. 30-Liam Lawson LAW.")
        st.write("Escuderia: Mercedes-AMG PETRONAS Formula One Team. Chasis:Mercedes W16 Motor: Mercedes-AMG F1 M16. Pilotos:63-George Russell RUS. 12-Andrea Kimi Antonelli ANT.")
        st.write("Escuderia: Aston Martin Aramco Formula One Team. Chasis: Aston Martin Aramco AMR25 Motor:Mercedes-AMG F1 M16. Pilotos:14-Fernando Alonso ALO. 18-Lance Stroll STR.")
        st.write("Escuderia: BWT Alpine Formula 1 Team. Chasis:Alpine A525. Motor: Renault E-Tech RE25. Pilotos: 10-Pierre Gasly GAS. 7-Jack Doohan DOO.")
        st.write("Escuderia: MoneyGram Haas F1 Team. Chasis: HaasVF-25. Motor:Ferrari 066/12 Pilotos:31-Esteban Ocon OCO. 87-Oliver Bearman BEA.")
        st.write("Escuderia:Visa Cash App Racing Bulls Formula One Team. Chasis: Racing Bulls VCARB 02. Motor: Honda RBPTH002. Pilotos: 22-Yuki Tsunoda TSU. 6-Isack Hadjar HAD.")
        st.write("Escuderia: Atlassian Williams Racing Chasis:Williams FW47. Motor: Mercedes-AMG F1 M16. Pilotos: 55-Carlos Sainz Jr. SAI. 23-Alexander Albon ALB.")
        st.write("Escuderia: Stake F1 Team Kick Sauber. Chasis: Kick Sauber C45. Motor: Ferrari 066/12 Pilotos: 27-Nico Hülkenberg HÜL. 5-Gabriel BortoletoBOR.")
    elif seleccion == "El Fin de Semana":
        st.write("Cada Gran Premio se divide en tres días, excepto los fines de semana con carreras Sprint (seis de las 24 rondas). Un programa tradicional de competencia se divide en:")
        st.write("* Día 1, con dos prácticas de entrenamiento de una hora cada una (Práctica Libre 1 y Práctica Libre 2);")
        st.write("* Día 2, con una sesión de entrenamientos de una hora (Práctica Libre 3), y una Clasificación, que se divide en tres etapas: Q1, Q2 y Q3, con una duración de 18, 15 y 12 minutos, respectivamente. En la Q1 se eliminan los cinco pilotos más lentos; otros cinco se eliminan en la Q2 y finalmente los 10 restantes pelean por las mejores posiciones de arranque en la Q3. El piloto más veloz arranca en el primer lugar de la parrilla, un lugar llamado “pole position”;")
        st.write("* Día 3, la carrera.")
    elif seleccion == "Gran Premio":
        st.write("La carrera de Fórmula 1 recibe por nombre “Gran Premio” y tiene una distancia mínima de 305 kilómetros, por lo que el número de vueltas dependerá de la longitud del autódromo. En el caso del Mexico GP, por ejemplo, se dan 71 vueltas al trazado de 4.3 kilómetros (305.3 kilómetros) del Autódromo Hermanos Rodríguez.Antes de comenzar la carrera, los pilotos dan una o más vueltas previo a colocarse en el cajón en el cual calificaron, a esos giros se les llama “vueltas de reconocimiento”. Una vez que se forman en la parrilla de salida, un semáforo con cinco luces rojas se va apagando, una a una, y cuando no existe ninguna encendida, se da el arranque.Gana el piloto en cumplir con la distancia pactada antes que el resto." )
    elif seleccion =="Puntos por Posición":
        st.write("Al tratarse de un campeonato y no sólo de una carrera, cada Gran Premio otorga puntos válidos para el torneo anual.")
        st.write("El primer lugar de cada competencia suma 25 puntos; el segundo lugar obtiene 18; el tercero, 15; el cuarto, 12; el quinto, 10; el sexto, 8; el séptimo, 6; el octavo, 4; el noveno, 2 y el décimo, 1. Se otorga un punto extra al piloto que consiga la vuelta más rápida en carrera, siempre y cuando termine entre los 10 primeros lugares.")
    elif seleccion =="Cambio de Neumáticos":
        st.write("Los equipos tienen permitido el cambiar neumáticos durante las sesiones y en la carrera. Los pilotos llevan los autos a pits, donde el equipo de mecánicos realiza el cambio. Las llantas sufren desgaste y pierden su desempeño óptimo, por tanto, los ingenieros desarrollan estrategias para obtener el mayor beneficio de los tiempos de vida de los neumáticos.")
        st.write("En cada carrera, Pirelli, la llantera oficial, otorga una variedad de tres compuestos distintos: blandos, medios y duros. Cada uno ofrece cualidades distintas en cuanto a agarre y duración, y serán los equipos los que decidan cuándo usarlos, de acuerdo a sus estrategias. Los neumáticos de Fórmula 1 se clasifican en tipos de seco y de lluvia. Los de seco se clasifican en duros, medios y blandos.")
        st.write("Neumáticos de pista seca.")
        st.write("Duro: Son de color blanco y aguantan más vueltas, pero tienen menor adherencia y prestaciones de velocidad.")
        st.write("Medio: Son una combinación de los duros y los blandos, y son una opción popular para condiciones de pista variables.")
        st.write("Blando: Son los más rápidos pero se desgastan rápidamente.")
        st.write("Neumáticos de pista mojada o lluvia.")
        st.write("Intermedios:Son de color verde y son ideales para condiciones de lluvia ligera o pista mojada sin demasiada acumulación de agua.")
        st.write("De lluvia extrema:Son de color azul y están diseñados para condiciones extremas, como lluvia abundante.")
        st.write("Los neumáticos se eligen en función de la estrategia de paradas del equipo, la posición en la que salga el coche, o las condiciones climatológicas en las que se va a correr.")
    elif seleccion =="Banderas":
        st.write("Los oficiales de pista se comunican con los pilotos con un sistema de banderas de colores, siendo la más utilizada la amarilla, que significa que hay un peligro en la pista. Puede ser un accidente o un auto lento o detenido, por citar un ejemplo. Cuando hay banderas amarillas agitándose en toda la pista, está prohibido rebasar.")
        st.write("La bandera roja significa que la carrera será detenida. Los autos se dirigen a pits y se detienen. Puede ser por algún objeto que obstruye la pista, o lluvia excesiva. La bandera a cuadros negros y blancos se puesta únicamente en el puesto de meta, y significa que la carrera ha terminado.")
        st.write("Existen otras banderas, como la azul, para anunciar que existe un auto más veloz y que hará un rebase, pero poco a poco las identificarás.")
    elif seleccion =="Techo Presupuestario":
        st.write("El límite de gastos en la Fórmula 1, o techo presupuestario, es lo que establece qué cantidad exacta de dinero puede gastar un equipo durante una temporada. En vigor desde 2021, la idea original era que estuviera situado en 175 millones de euros pero, con la irrupción de la pandemia, lo que provocó que algunas de las escuderías tuvieran gastos inasumibles, se decidió reducirlo a 125 millones de euros.")
        st.write("Asimismo, dentro del plan estaba contemplado que se fuera reduciendo en cinco millones en los dos años siguientes, pero después de la alucinante subida de precios de la economía mundial durante 2022, se produjeron algunos ajustes para proporcionar el límite con la inflación generada.")
        st.write("El techo presupuestario se introdujo en la Fórmula 1 con el objetivo de acabar con el gasto, prácticamente ilimitado, del que disponían algunos equipos, mientras que otros, con un presupuesto mucho menor, se veían obligados a hacer malabares para, al final, no poder competir en pista.")
        st.write("Así, este límite busca nivelar las condiciones dentro de la pista lo máximo posible entre todos los equipos para, así, garantizar el espectáculo deportivo cada fin de semana. Además, y como complemento, trata de asegurar la supervivencia de todas las escuderías de la parrilla.")
        st.write("En el límite de gastos de la Fórmula 1 entra cualquier gasto que se pueda relacionar con el rendimiento del monoplaza, más allá de los motores. Por tanto, en el límite presupuestario de la Fórmula 1 se incluye lo siguiente:")
        st.write("Las piezas del monoplaza.")
        st.write("Los elementos necesarios para el funcionamiento del coche.")
        st.write("Todo el personal del equipo.")
        st.write("Todo el equipamiento del garaje.")
        st.write("Todos los recambios de los monoplazas.")
        st.write("Gasto de transporte.")
        st.write("Además de todo ello, y para garantizar el correcto cumplimiento, la FIA exige que los equipos decidan qué desarrollan del monoplaza y cómo lo llevan a cabo, detallando cuál es el gasto de cada pieza que se fabrica, cuantas piezas necesitan y cuál es el saldo de sus cuentas.")
        st.write("De igual forma, hay otros aspectos que no se incluyen dentro del límite de gastos de las escuderías de Fórmula 1. Esto es:")
        st.write("El salario de los pilotos.")
        st.write("El salario de los tres miembros del personal mejor pagados.")
        st.write("Los gastos de viaje.")
        st.write("El marketing.")
        st.write("Los costes inmobiliarios y legales.")
        st.write("Derechos de licencias.")
        st.write("La actividad no relacionada con la Fórmula 1.")
        st.write("Pagos por paternidad o enfermedad.")
        st.write("Primas de empleados y prestaciones médicas.")