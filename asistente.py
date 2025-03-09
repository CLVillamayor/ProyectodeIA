import streamlit as st
import requests

# Configuración de la API de Groq
groq_api_key = "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"
groq_url = "https://api.groq.com/openai/v1/chat/completions"

# Función para realizar la consulta a la API de Groq
def consulta_groq(pregunta):
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    query = {
        "model": "mixtral-8x7b-32768",
        "messages": [{"role": "user", "content": pregunta}],
        "temperature": 0.7
    }
    response = requests.post(groq_url, headers=headers, json=query)
    return response.json()

# Función para procesar la respuesta de la API de Groq
def procesa_respuesta(respuesta):
    if "choices" in respuesta and len(respuesta["choices"]) > 0:
        result = respuesta["choices"][0]
        if "message" in result and "content" in result["message"]:
            return result["message"]["content"]
    return "Lo siento, no pude encontrar una respuesta"

# Interfaz del asistente virtual
def main():
    st.title("Asistente virtual de F1 Manijita")
    st.warning("La información proporcionada por este asistente virtual puede no ser actual.")
    pregunta = st.text_input("Pregúntame algo sobre F1 Manijita")

    if pregunta:
        respuesta = consulta_groq(pregunta)
        resultado = procesa_respuesta(respuesta)
        #st.write(f"Respuesta sin procesar: {respuesta}")
        st.write(f"Respuesta procesada: {resultado}")