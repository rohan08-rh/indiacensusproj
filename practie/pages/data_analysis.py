import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
final_df=pd.read_csv('india.csv')
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    return pd.read_csv("data/india.csv")
final_df.set_index('State name',inplace=True)
st.title('Analysis of Cencus Data of India')
st.write('You can analyse the data according to your choice of parameters and states')
col1,col2,col3=st.columns(3)
with col1:
   a=st.selectbox('Select the state',final_df['State'].unique().tolist())
with col2:   
    b=st.selectbox('Select the primary parameter',sorted(final_df.columns[3:]))
    
with col3:
     c=st.selectbox('Select the secondary parameter',sorted(final_df.columns[3:]))
if a and b:
      state_df=final_df[final_df['State']==a]
      st.dataframe(state_df[b])
if a and b and c:
      st.dataframe(state_df[[b,c]])
