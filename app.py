import streamlit as st

# pip install openai langchain

import os
import streamlit as st

################## Langchain Code ######################

import openai

from langchain import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# pip install openai langchain

from apikey import openaikey

openai.api_key = openaikey

os.environ['OPENAI_API_KEY'] = openaikey

def openai_template(input1, input2, input3,):
    chat = ChatOpenAI(temperature=0.7, model="gpt-3.5-turbo-1106") # Here temperature is set to temp to provide a balanced response
    ### Template for the system message
    template = """
    You are a helpful travel assistant.
    """
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    human_template = f""""
    Suggest 3 holiday plans for someone called{input1}, who is {input2} years old, and is interested in {input3}
    """

    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])

    chain = LLMChain(llm=chat, prompt=chat_prompt)
    result = chain.run({"input1": input1, "input2": input2, "input3": input3})
    return result

################# Streamlit Code ######################

st.title("Hello World")

with st.form(key='my_form'):
    name = st.text_input(label="What's your name?")
    age = st.number_input(label="What's your age?")
    interest = st.text_input(label="What are you interested in?")
    submit_button = st.form_submit_button(label='Submit')

if submit_button:
    response = openai_template(name, age, interest)
    st.write(f"Here are 3 great ideas for your holiday:\n {response}") 