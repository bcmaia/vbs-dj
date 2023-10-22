import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import tempfile
from youtube_search import YoutubeSearch
from pytube import YouTube
import ffmpeg

@st.cache_data
def get_audio(query : str):
    results = YoutubeSearch(query, max_results=10).to_dict()
    link = 'https://www.youtube.com/watch?v=' + results[0]['id']
    yt = YouTube(link)

    stream_url = yt.streams.all()[0].url 
    audio, err = (
        ffmpeg
        .input(stream_url)
        .output("pipe:", format='wav', acodec='pcm_s16le')
        .run(capture_stdout=True)
    )

    return audio

def show_audioplayer(query : str):
    audio = get_audio(query)
    st.audio(audio, format='audio/wav')
