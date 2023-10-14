import dataiku
import streamlit as st
import pandas as pd 
import amd_st

def selecting_QuerPoints():
    query, proj = st.columns(2)
    project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
    vars = project_handle.get_variables()['standard']
    queryType = vars['query_options']

    with query:
        st.title('Choosing Query type')
        input_queryType = st.radio("State how the Query will be done", queryType)

    with proj:
        st.title('Select a Project')
        selected_project = st.selectbox('Select', options = [config['name'] for config in vars['configuration']])
        index = [index for index, project in enumerate(vars['configuration']) if selected_project == project['name']][0]
        focusProject = vars['configuration'][index]

    query_return_value = pd.DataFrame([[selected_opn, selcted_LotID, selcted_KDF, selcted_QueryID, selcted_LocalCSV, selcted_localKDF]], columns=queryType)
    
    selected_QueryType = query_return_value[input_queryType]
    
    return focusProject, selected_QueryType

def selected_opn(): 
    return 1
def selcted_LotID(): 
    return 2
def selcted_KDF(): 
    return 3
def selcted_QueryID(): 
    return 4
def selcted_LocalCSV(): 
    return 5
def selcted_localKDF(): 
    return 6