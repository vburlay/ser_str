import streamlit as st
import urllib3
from streamlit_imagegrid import streamlit_imagegrid
import requests
import pandas as pd
import plotly.express as px
url = 'https://raw.githubusercontent.com/vburlay/ser_str/master/date/model_result.csv'

data = pd.read_csv(url, index_col=0)
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
            fig = px.bar(data['classification'],width=1000,height=500)
            st.plotly_chart(fig)
        with tab2:
                fig = px.scatter(
                    data.drop(columns=['file']), width=1000, height=650
                )
                st.plotly_chart(fig)
        with tab3:
            fig = px.bar(data)
            st.dataframe(data,width=1200,height=600)




elif add_selectbox == "Show the source code" :
    http = urllib3.PoolManager()
    response = http.request('GET','https://raw.githubusercontent.com/vburlay/ser_str/master/workflow/streamlit.md')
    readme_text = st.markdown(response.data.decode("utf-8"))