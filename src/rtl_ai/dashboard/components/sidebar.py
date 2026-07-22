import streamlit as st

def render_sidebar():
    st.sidebar.header("Navigation")
    st.sidebar.selectbox("Analysis Type",["LINT","CDC","RDC"])
