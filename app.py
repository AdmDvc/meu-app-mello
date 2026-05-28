import streamlit as st
import google.generativeai as genai

st.title("Meu Assistente Pessoal")

# Cole a sua API Key entre as aspas abaixo
genai.configure(api_key="AIzaSyDw0m23du2RWV8M_R6HBfgls5yhiKz4Abs")
model = genai.GenerativeModel('gemini-1.5-flash')

pergunta = st.text_input("Como posso ajudar?")
if st.button("Enviar"):
    if pergunta:
        resposta = model.generate_content(pergunta)
        st.write(resposta.text)