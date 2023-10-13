import streamlit as st
import pandas as pd
from introduction import intro
from run_fusecol import run_FuseCOL

import streamlit as st

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# st.set_page_config(layout="wide")

page_names_to_funcs = {
    # "Introduction": intro,
    "fuseCOL": run_FuseCOL,
    # "Mapping Demo": mapping_demo,
    # "DataFrame Demo": data_frame_demo
}

demo_name = st.sidebar.selectbox("Choose a Tab", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()