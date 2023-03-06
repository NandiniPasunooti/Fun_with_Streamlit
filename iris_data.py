import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px


st.title("Dashboard - Iris Data")

img = image.imread(r"C:\Users\user\internship\Info of St\images\iris.jpg")
st.image(img)

df = pd.read_csv(r"C:\Users\user\internship\Info of St\data\iris.csv")
st.dataframe(df)

species = st.selectbox("Select the Species:", df['Species'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Species'] == species], x="SepalLengthCm")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Species'] == species], y="SepalLengthCm")
col2.plotly_chart(fig_2, use_container_width=True)