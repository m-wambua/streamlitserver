import streamlit as st 
import pandas as pd
'''
with st.sidebar:
    st.title('Dexter Labs')
    choice=st.radio('Navigation',['Upload','Profiling','ML','Download'])
    st.info('This application allows you to build an automated ML pipeline ')
'''
choice=('Navigation',['Upload','Profiling','ML','Download'])

if choice=='Upload':
    st.title('Upload your data for modelling')
    file=st.file_uploader('Upload your Dataset here')
    if file:
        pass

if choice == 'Profiling':
    pass

if choice ==' ML':
    pass
if choice == 'Download':
    pass

