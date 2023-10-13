import streamlit as st


def intro():
    st.sidebar.success("Select a demo above.")

    st.markdown("""
# FuseCOL

OPN &rarr; Given an OPN will query based on the OPN based on the days given  
KDF Name &rarr; Give it the name of the KDF, if in ULSD will query for it using AmdMap  
Local KDF &rarr; Not yet working, will search in the kdf folder for kdf and parse the fuserams and perform the analysis  
Local CSV &rarr; Input the file name that you will be querying. If you gathered your input from nemawashi/snowflake  

    """)