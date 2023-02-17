import streamlit as st
import urllib3
from streamlit_imagegrid import streamlit_imagegrid
import requests
from pathlib import Path
import torch

st.sidebar.title("Control Panel")
class_names = ['neutral', 'happy', 'sad', 'angry', 'fear', 'surprise']
classification = []
percentages_0 = []
percentages_1 = []
percentages_2 = []
percentages_3 = []
percentages_4 = []
percentages_5 = []

# load model
model = torch.load("https://raw.githubusercontent.com/vburlay/ser_str/master/workflow/models/audio_model.pth")



with st.sidebar:
    add_selectbox = st.selectbox("App-Mode", ["Application start","Show the source code"])
    add_radio = st.radio(
        "Model 👇",
        ["Pytorch (ResNet34)"])


if add_selectbox  == "Application start":

    st.title("Speach emotion recognition")
    if  st.checkbox("Show raw data"):

        zoom_val = st.sidebar.slider('Zoom', 183, 240)

        urls = [
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-09.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-10.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-11.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-12.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-13.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-14.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-15.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-16.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-17.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-18.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-19.wav.png"
            },
            {
                "width": 2000,
                "height": 2000,
                "src": "https://raw.githubusercontent.com/vburlay/ser_str/master/date/test/test50_03-01-01-01-02-02-20.wav.png"
            }
        ]

        return_value = streamlit_imagegrid(urls=urls, zoom=zoom_val, height=1000)

        if return_value is not None:
            response = requests.get(return_value)
            st.sidebar.markdown('<img src={} width=240px></img>'.format(return_value), unsafe_allow_html=True)
    else:
        tab1, tab2, tab3 = st.tabs(["Countplot of the results", "Result Tabular","Individual results"])
        with tab1:
            st.title(Path.cwd()/ 'temp' / 'workflow' / 'www' / 'audio_pth')


elif add_selectbox == "Show the source code" :
    http = urllib3.PoolManager()
    response = http.request('GET','https://raw.githubusercontent.com/vburlay/ser_str/master/workflow/streamlit.md')
    readme_text = st.markdown(response.data.decode("utf-8"))