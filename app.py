"./app.py"

import streamlit as st
from main import chain, retriever

st.title("Anshu Kumar - AI Career Agent")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process input
if prompt := st.chat_input("Ask me about my experience..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        docs = retriever.invoke(prompt)
        # Using your chain logic
        response = chain.invoke({"docs": docs, "question": prompt})
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})