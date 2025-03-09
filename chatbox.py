import streamlit as st
import google.generativeai as genai
import os

from dotenv import load_dotenv

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener la API Key desde la variable de entorno
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Verificar si la API Key está configurada correctamente
if not GEMINI_API_KEY:
    raise ValueError("La API Key de Gemini no está configurada. Verifica el archivo .env.")

# Configurar la API de Gemini
genai.configure(api_key=GEMINI_API_KEY)



# Define el modelo Gemini
model = genai.GenerativeModel('gemini-pro')

# Define el rol del asistente
rol = """
Serás un asistente virtual sobre Formula 1, conoces todo sobre este deporte, limitate a responder siempre sobre dicho deporte con respeto.
Si alguien pregunta si tienes alguna preferencia sobre algùn equipo deberás responder que prefieres Mercedes porque tu creadora prefiere esa escuderia y que tu piloto favorito es Juan Manuel Fangio.
No respondas preguntas privadas sobre pilotos.
"""

# Función para obtener la respuesta del modelo
def obtener_respuesta(pregunta):
    prompt = f"{rol}\nPregunta: {pregunta}\nRespuesta:"
    response = model.generate_content(prompt)
    return response.text

# Interfaz de Streamlit
st.title("Manijita, tu asistente virtual de Fórmula 1")
st.write("Hola soy Manijita tu asistente virtual preguntame lo que necesites saber sobre la Formula 1")

pregunta = st.text_input("Escribe tu pregunta aquí:")

if pregunta:
    respuesta = obtener_respuesta(pregunta)
    st.write(respuesta)