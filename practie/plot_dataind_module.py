import pandas as pd
import plotly.express as px
import streamlit as st


def render_plot_dataind():
    final_df = pd.read_csv('india.csv')
    final_df.set_index('State name', inplace=True)

    st.subheader('All-India Visualization')
    st.markdown('This view is shown only after the button is clicked.')

    fig = px.scatter_mapbox(
        final_df,
        lat='Latitude',
        lon='Longitude',
        size='Population',
        color='State',
        zoom=3,
        mapbox_style='carto-positron',
        width=1200,
        height=600,
        hover_name='State',
    )
    st.plotly_chart(fig, use_container_width=True)
