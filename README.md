# Graph_app
import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('C:/Users/Checkout/Fish.csv')

Fig = px.bar(df, x= 'Species', y = 'Weight', title = 'Bar plot depicting weights of different fish species')

st.plotly_chart(Fig)
