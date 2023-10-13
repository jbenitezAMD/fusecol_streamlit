import dataiku
import streamlit as st
import pandas as pd
from fusecol_interface.editing_query_points import editing_QuerPoints
from fusecol_interface.selecting_query_points import selecting_QuerPoints
from fusecol_interface.submitting_query_points import submit_QueryPoints

def run_FuseCOL():

    select_query, editing_query, submit_query = st.tabs(['Select Query Points', 'Edit Query Points', 'Submit Query'])
    focusProject = ''
    # st.sidebar.markdown(
    #     """
    #     ## fuseCOL
    #     --- 
    #     """)
    with select_query: focusProject, selected_Query_Type = selecting_QuerPoints()
    with editing_query: editing_QuerPoints(focusProject)
    with submit_query: submit_QueryPoints(focusProject, selected_Query_Type)
