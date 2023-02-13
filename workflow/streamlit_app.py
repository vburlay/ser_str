"""
Created on Sat Feb 03 23:41:46 2023

@author: Vladimir
"""
import streamlit as st
import pandas as pd
import skript_audio_class

data = pd.DataFrame(data=skript_audio_class.check_wav("www/audio"))
st.title("SER")
st.subheader("Raw data")
st.write(data)
