import streamlit as st
import time

# Create a Streamlit web app
st.title("Streamlit App with Tags")

# Add a text input field
user_input = st.text_input("Enter some text:", "")

# Add a button
if st.button("Submit"):
    st.write("You entered:", user_input)

# Define a list of predetermined tags
tag_list = ["Tag1", "Tag2", "Tag3", "Tag4", "Tag5"]

# Add a tag selection field
selected_tags = st.multiselect("Select tags:", tag_list)

if selected_tags:
    st.write("Selected Tags:", selected_tags)

# Add a progress bar
progress = st.progress(0)
for i in range(101):
    progress.progress(i)
    time.sleep(0.1)  # Simulating some time-consuming task

# Add a slider
slider_value = st.slider("Moods:", min_value=0, max_value=100, value=50)
slider_value = st.slider("Genrers:", min_value=0, max_value=100, value=50)

st.write("Slider Value:", slider_value)
