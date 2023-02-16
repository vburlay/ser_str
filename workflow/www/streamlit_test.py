import streamlit as st
import urllib
from streamlit_imagegrid import streamlit_imagegrid
import requests
def get_file_content_as_string(path):
    url = 'https://raw.githubusercontent.com/vburlay/ser_str/master/workflow/' + path
    response = urllib.request.urlopen(url)
    return response.read().decode("utf-8")

st.sidebar.title("Control Panel")

with st.sidebar:
    add_selectbox = st.selectbox("App-Mode", ["Application start","Show the source code"])
    add_radio = st.radio(
        "Choose a model",
        ("Pytorch (ResNet34)", "Keras (ResNet34)")   )

    if add_selectbox == "Application start" and add_radio == "Pytorch (ResNet34)":

        st.title("Speach emotion recognition")
        if not st.checkbox("Show raw data"):

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