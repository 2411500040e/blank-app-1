import streamlit as st
import pandas as pd

df = pd.read_excel('analisis_ulasan_shopee.xlsx')

st.title("Analisis Ulasan Shopee")
st.write("Menampilkan beberapa baris data:")
st.dataframe(df.head(50))
