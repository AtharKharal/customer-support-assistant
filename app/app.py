import streamlit as st
from retriever import Retriever
from generator import Generator

st.title("Free AI Customer Support Assistant")

retriever = Retriever()
generator = Generator()

st.write("Type a question related to the FAQ and press Enter.")
query = st.text_input("Ask me something:", placeholder="e.g. What is your return policy?")

if query:
    results = retriever.search(query, k=1)
    context = results[0][1]  # take top answer
    answer = generator.generate(query, context)
    st.subheader("Answer")
    st.write(answer)
