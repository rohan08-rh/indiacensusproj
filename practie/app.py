import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
final_df=pd.read_csv('india.csv')
final_df.set_index('State name',inplace=True)
list_of_states=final_df['State'].unique().tolist()
list_of_states.insert(0,'Overall')
st.title('INDIA CENCUS DATA ANALYSIS')
st.subheader('Welcome to Cencus Data Analysis of India 2011 Cencus Portal')
st.markdown('This portal helps you to analyze the cencus data of india in a very interactive way')
st.sidebar.title('India Cencus Analysis')


st.sidebar.subheader('Select the state')
state=st.sidebar.selectbox('State',list_of_states)
primary=st.sidebar.selectbox('Select Primary Parameter',sorted(final_df.columns[3:]))

secondary=st.sidebar.selectbox('Select Secondary Parameter',sorted(final_df.columns[3:]))


plot=st.sidebar.button('Vizualize the data')

if plot:
    if(state=='Overall'):
        fig=px.scatter_mapbox(final_df,lat='Latitude',lon='Longitude',size=primary,color=secondary,
                              zoom=3, mapbox_style='carto-positron',width=1200,height=600,hover_name='State')
        #india
        st.plotly_chart(fig,use_container_width=True)
    else:  
        state_df=final_df[final_df['State']==state]
        fig=px.scatter_mapbox(state_df,lat='Latitude',lon='Longitude',size=primary,color=secondary,
                              zoom=3, mapbox_style='carto-positron',width=1200,height=600,hover_name='District name')
        #india
        st.plotly_chart(fig,use_container_width=True)