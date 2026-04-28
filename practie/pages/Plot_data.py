import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plot_dataind_module import render_plot_dataind

final_df = pd.read_csv('india.csv')
state = final_df.groupby('State name')

if 'active_mode' not in st.session_state:
    st.session_state.active_mode = None

if 'show_plot_dataind' not in st.session_state:
    st.session_state.show_plot_dataind = False


def popp(pop):
    st.subheader('top 10 most Populated states')
    pop=state['Population'].sum().sort_values(ascending=False).head(10)
    figg=px.bar(x=pop.index,y=pop.values,log_y=True)
    st.plotly_chart(figg, use_container_width=True)

def dempfeatres(smt):
    st.subheader('Demographic Parameters')
    state = final_df.groupby('State name')
    s = state[['Age_Group_0_29', 'Age_Group_30_49', 'Age_Group_50', 'Age not stated']].sum()
    state_wise = s.loc[smt]
    fig0 = px.pie(
        values=state_wise.values,
        names=state_wise.index,
        title=f'Age structure of {smt}',
        hover_name=state_wise.index,
    )
    st.plotly_chart(fig0, use_container_width=True)
def literacy(r):
    fm=final_df.groupby('State name')[['Male_Literate','Female_Literate']].sum()
    data=fm.loc[r]
    fig=go.Figure()
    fig.add_trace(go.Bar(x=data.index,y=data.values,name='male_Literate'))
    fig.add_trace(go.Bar(x=data.index,y=data.values,name='female_Literate'))
    fig.update_layout(title=f'Male vs Female Literacy in {r}',xaxis_title='Category',yaxis_title='Population',barmode='group')
    st.plotly_chart(fig,use_container_width=True)    
def sexratio(ratio):
    fm=final_df.groupby('State name')[['Male','Female']].sum()
    data=fm.loc[ratio]
    fig=go.Figure()
    fig.add_trace(go.Bar(x=data.index,y=data.values,name='male'))
    fig.add_trace(go.Bar(x=data.index,y=data.values,name='female'))
    fig.update_layout(title=f'Male vs Female population in {ratio}',xaxis_title='Category',yaxis_title='Population',barmode='group')
    st.plotly_chart(fig,use_container_width=True)

def set_active_mode(mode):
    st.session_state.active_mode = mode


st.title('Vizualize the data')

if st.button('Plot Data on all over India'):
    st.session_state.show_plot_dataind = True

if st.session_state.show_plot_dataind:
    def hide_plot_dataind():
        st.session_state.show_plot_dataind = False

    st.button('Hide All-India Plot', on_click=hide_plot_dataind)
    render_plot_dataind()

st.subheader('You can analyse the data according to your choice of Parameters and states')
st.markdown('Select the parameters')

col11, col22, col33 = st.columns(3)
with col11:
    st.button('Demographic Parameters', on_click=set_active_mode, kwargs={'mode': 'dem'})
with col22:
    st.button('Social Parameters', on_click=set_active_mode, kwargs={'mode': 'soc'})
if st.session_state.active_mode == 'dem':
    smt = st.selectbox('Select the state', final_df['State name'].unique().tolist(), key='dem_state')
    if smt:
        dempfeatres(smt)
    pop = st.selectbox('Select the population parameter',['overall population'])
    if pop:
        popp(pop)
    ratio=st.selectbox('Select the state',final_df['State name'].unique().tolist())
    if ratio:
        sexratio(ratio)

elif st.session_state.active_mode == 'soc':
    r=st.selectbox('Select the state',final_df['State name'].unique().tolist())
    st.header('Literacy Rate')
    if r:
        literacy(r)
     

