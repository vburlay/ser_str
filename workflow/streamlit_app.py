"""
Created on Sat Feb 03 23:41:46 2023

@author: Vladimir
"""
import streamlit as st
import pandas as pd
import skript_audio_class
import plotly.express as px
from streamlit_imagegrid import streamlit_imagegrid
import requests
from PIL import Image
from io import BytesIO


st.sidebar.title("Control Panel")

with st.sidebar:
    add_selectbox = st.selectbox("App-Mode", ["Application start","Show the source code"])
    add_radio = st.radio(
        "Choose a model",
        ("Pytorch (ResNet34)", "Keras (ResNet34)")   )


if add_selectbox  == "Application start" and add_radio == "Pytorch (ResNet34)":
    data = pd.DataFrame(data=skript_audio_class.check_wav("www/audio"))
    st.title("Speach emotion recognition")
    if  st.checkbox("Show raw data"):

        zoom_val = st.sidebar.slider('Zoom', 198, 240)

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
        fig = px.bar(data)

        tab1, tab2, tab3 = st.tabs(["Countplot of the results", "Result Tabular","Individual results"])
        with tab1:
            st.plotly_chart(fig)
        with tab2:
            st.dataframe(data,width=1200,height=600)
        with tab3:
            st.write(data)

elif add_selectbox == "Show the source code" and  add_radio == "Pytorch (ResNet34)":
    print('continios')
else:
    st.title("Keras (ResNet34) is not jet included")

