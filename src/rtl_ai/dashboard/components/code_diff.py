import streamlit as st

def show_diff(original, repaired):
    st.subheader("RTL Code Diff")
    st.code(original, language="verilog")
    st.code(repaired, language="verilog")
