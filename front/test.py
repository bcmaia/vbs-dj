import streamlit as st
import time
import pandas as pd

# Define your music_queue of tuples (name, duration)
music_queue = [
    {"track_name": "Song 1", "len": 5.7},
    {"track_name": "Song 2", "len": 2.7},
    {"track_name": "Song 2.5", "len": 70.7},
    {"track_name": "Song 3", "len": 10.7},
]

music_pool = [
    {"track_name": "Song 1", "len": 5.7},
    {"track_name": "Song 2", "len": 2.7},
    {"track_name": "Song 2.5", "len": 70.7},
    {"track_name": "Song 3", "len": 10.7},
]



# Initialize app state
@st.cache_resource
def get_state():
    return {
        "music_queue": music_queue,
        "current_song": None,
        "played_songs": [],
        "progress": 0,
        "is_playing": False,
        "error_msg": None,
        "searching": False,
    }

# @st.cache_resource
# def update_state(state, key, value):
#     state[key] = value

state = get_state()

# Define Streamlit layout
st.title("Music Player App")

# Slots
slot_curr_playing = st.empty()
slot_progress_bar = st.empty()
slot_err = st.empty()

# Buttons here
btn_cols = st.columns(6, gap="small")


# Display the music_queue

# st.write(state["music_queue"])

slot_queues = st.columns(2)

def pĺay():
    if state["is_playing"]: return
    if state["current_song"] is None:
        state["current_song"] = state["music_queue"].pop(0)
    state["is_playing"] = True

def pause():
    state["is_playing"] = False

def play_previus():
    # if not state["is_playing"]: return
    if not state["played_songs"]: return False

    if state['progress'] > 10 and state["current_song"] and state["current_song"]['len'] > 50.0:
        state['progress'] = 0
        return True

    if state["current_song"]: state["music_queue"].insert(0, state["current_song"])
    state["current_song"] = state["played_songs"].pop()
    state['progress'] = 0

    return True

def play_next():
    # if not state["is_playing"]: return
    if not state["music_queue"]: return False

    if state["current_song"]: state["played_songs"].append(state["current_song"])
    state["current_song"] = state["music_queue"].pop(0)
    state['progress'] = 0

    return True

if state['error_msg']:
    with slot_err:
        st.write(state['error_msg'])

# Play, Stop, Next, and Previous buttons
with btn_cols[0]:
    if st.button("Play"):
        pĺay()

with btn_cols[1]:
    if st.button("Pause"):
        state["is_playing"] = False

with btn_cols[2]:
    if st.button("Next"):
        play_next()

with btn_cols[3]:
    if st.button("Previous"):
        play_previus()

# Update progress bar
if state["is_playing"]:
    if state["progress"] < 100:
        state["progress"] += 1
    else:
        state["played_songs"].append(state["current_song"])
        if state["music_queue"]:
            state["current_song"] = state["music_queue"].pop(0)
        else:
            state["current_song"] = None
        state["progress"] = 0

# Display the currently playing and played songs
if state["current_song"]:
    with slot_curr_playing:
        st.write("Currently Playing: " + state["current_song"]['track_name'])

if state["music_queue"]:
    with slot_queues[0]:
        st.write("Music Queue:")
        st.dataframe(pd.DataFrame(state['music_queue']))

if state["played_songs"]:
    with slot_queues[1]:
        st.write("You've listened:")
        st.dataframe(pd.DataFrame(state['played_songs']))












# Create a Streamlit web app
st.header("What are you looking for?")

# Add a text input field
st.write("Use the text box to type a music name or to specify which kind of music/artist you are looking fore, if you think its needed.")
user_input = st.text_input("Enter a prop text:", "")

# Add a button
cols = st.columns(5)
with cols[0]:
    if st.button("Search"):
        st.write("You entered:", user_input)

with cols[1]:
    if st.button("Execute"):
        st.write("You entered:", user_input)

# Define a list of predetermined tags
genres_tag_list = ["Pop", "Rock", "Ambience", "Jass", "CyberPhonk"]
moods_tag_list = ["Sad", "Eletric", "Moody", "Relax", "Anger"]

# Add a tag selection field
selected_genres = st.multiselect("Genres", genres_tag_list)
selected_moods = st.multiselect("Moods", moods_tag_list)


if selected_genres:
    st.write("Selected Tags:", selected_genres)

# Add a slider
# slider_value = st.slider("Moods:", min_value=0, max_value=100, value=50)

# slider_value = st.slider("Genrers:", min_value=0, max_value=100, value=50)

# st.write("Slider Value:", slider_value)

def dataframe_with_selections(df):
    df_with_selections = df.copy()
    df_with_selections.insert(0, "Select", False)

    # Get dataframe row-selections from user with st.data_editor
    edited_df = st.data_editor(
        df_with_selections,
        hide_index=True,
        column_config={"Select": st.column_config.CheckboxColumn(required=True)},
        disabled=df.columns,
    )

    # Filter the dataframe using the temporary column, then drop the column
    selected_rows = edited_df[edited_df.Select]
    return selected_rows.drop('Select', axis=1)

selection = dataframe_with_selections(df)



















# Progress bar
if None != state["current_song"]:
    progress = None
    with slot_progress_bar: progress = st.progress(state['progress'])
    step = state["current_song"]['len'] / 100
    if state["is_playing"]:
        for i in range(state['progress'], 101):
            progress.progress(i)
            time.sleep(step)
            state["progress"] = i
            if (i >= 100):
                play_next()
                st.rerun()

