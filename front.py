import streamlit as st
from chatbot import predict_class, get_response, intents

st.title("Asistente de la clase IA y mini robots")

if "messages" not in st.session_state:
    st.session_state.messages = []

if "first_message" not in st.session_state:
    st.session_state.first_message = True

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.first_message:
    with st.chat_message("assistant"):
        st.markdown(
            "¡Hola! Soy tu asistente virtual para la clase de IA y mini robots. "
            "Estoy aquí para ayudarte con cualquier duda que tengas sobre el curso, "
            "los proyectos de mini robots o cualquier otro tema relacionado. "
            "¿En qué puedo ayudarte hoy?"
        )

    st.session_state.messages.append({"role": "assistant", "content": "¡Hola! Soy tu asistente virtual para la clase de IA y mini robots."})
    st.session_state.first_message = False

if prompt := st.chat_input("Escribe tu mensaje aquí..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    insts = predict_class(prompt)
    res = get_response(insts, intents)

    with st.chat_message("assistant"):
        st.markdown(res)

    st.session_state.messages.append({"role": "assistant", "content": res})