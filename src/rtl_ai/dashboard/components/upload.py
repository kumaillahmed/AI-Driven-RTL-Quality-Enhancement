import streamlit as st

def upload_logs():
    return st.file_uploader(
        "Upload RTL verification logs",
        type=["log","txt"]
    )
