#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.express as px
import streamlit as st
import pandas as pd

df = pd.read_csv('Fish.csv')

Fig = px.bar(df, x= 'Species', y = 'Weight')
st.plotly_chart(fig)


# In[ ]:




