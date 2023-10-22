import streamlit as st
import pandas as pd

# Create an initial DataFrame
data = {'Strings': []}

@st.cache_resource
def get_state():
    return {
        'l': []
    }

state = get_state()

# Function to add a new row to the DataFrame
@st.cache_resource
def add_row(state, string):
    state['l'] = state['l'] + [string]

# Streamlit app
st.title("Dynamic DataFrame Example")

# Input field for entering a new string
new_string = st.text_input("Enter a string:")

# Button to add the entered string to the DataFrame
if st.button("Add String"):
    if new_string:
        add_row(state, new_string)

# Display the current DataFrame
st.dataframe(pd.DataFrame(state['l'], columns=['aaaaaa']))
