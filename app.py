import streamlit as st
import openai
def ask_question(question):
    openai.api_key = "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"
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="act as a lawyer specialist on the ESMA guidelines, your answer should be only related to this regulation, you are prohibited to talk about any other subject. Here is my question: " + question,
    max_tokens=200,
    temperature=0
    )
    return response.choices[0].text 

inputfield = st.text_input('Enter your Question:', '')
st.write(ask_question(inputfield))
