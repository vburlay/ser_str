import streamlit as st
import urllib3
from streamlit_imagegrid import streamlit_imagegrid
import requests

st.sidebar.title("Control Panel")

with st.sidebar:
    add_selectbox = st.selectbox("App-Mode", ["Application start","Show the source code"])
    add_radio = st.radio("Choose a model",("Pytorch (ResNet34)") )


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



elif add_selectbox == "Show the source code" :
    url = 'https://raw.githubusercontent.com/vburlay/ser_str/master/workflow/streamlit.md'
    response = urllib3.request.urlopen(url)
    readme_text = st.markdown(response.read().decode("utf-8"))