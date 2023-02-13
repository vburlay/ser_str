"""
Created on Sat Feb 03 23:41:46 2023

@author: Vladimir
"""
from os.path import dirname, abspath, join
import sys
import streamlit as st
import pandas as pd
import numpy as np

# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '../../pythonProject/ser_streamlit', 'code'))
sys.path.append(CODE_DIR)
import skript_audio_class
# Give our app a title
st.title("SER")
data = pd.DataFrame(data=skript_audio_class.check_wav("www/audio"))
st.subheader("Raw data")
st.write(data)