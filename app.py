import streamlit as st
import pandas as pd
from introduction import intro
from fusecol_intterface.run_fusecol import run_FuseCOL

st.set_page_config(layout="wide")

page_names_to_funcs = {
    "Introduction": intro,
    "fuseCOL": run_FuseCOL,
    # "Mapping Demo": mapping_demo,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a Tab", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()