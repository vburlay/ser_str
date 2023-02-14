"""
Created on Sat Feb 03 23:41:46 2023

@author: Vladimir
"""
import streamlit as st
import pandas as pd
import skript_audio_class
import plotly.express as px

class_names = ['neutral', 'happy', 'sad', 'angry', 'fear', 'surprise']
st.sidebar.title("Control Panel")
#app_mode = st.sidebar.selectbox("App-Mode", ["Application start","Show the source code"])
with st.sidebar:
    add_selectbox = st.selectbox("App-Mode", ["Application start","Show the source code"])
    add_radio = st.radio(
        "Choose a model",
        ("Pytorch (ResNet34)", "Keras (ResNet34)")   )


if add_selectbox  == "Application start" and add_radio == "Pytorch (ResNet34)":
    data = pd.DataFrame(data=skript_audio_class.check_wav("www/audio"))
    st.title("Speach emotion recognition")
    if st.checkbox("Show raw data"):
        st.subheader("Raw data")
       # st.write(data)
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

