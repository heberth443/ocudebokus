import streamlit as st

st.set_page_config(page_title="Weduka", layout="wide")

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=800, scrolling=False)
