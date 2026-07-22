import streamlit as st

st.set_page_config(page_title="RTL AI Dashboard", layout="wide")
st.title("AI-Driven RTL Quality Enhancement")
st.write("Upload LINT, CDC or RDC reports to begin analysis.")
uploaded = st.file_uploader("Upload verification report")
if uploaded:
    st.success(f"Loaded: {uploaded.name}")
