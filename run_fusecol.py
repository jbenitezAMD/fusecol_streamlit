import dataiku
import streamlit as st
import pandas as pd
import json


def run_FuseCOL():

    # with st.echo():
    # jls_extract_var = write
    st.write(f"streamlit version: {st.__version__}")

    focusProject = ''
    st.sidebar.markdown(
        """
        ## fuseCOL
        --- 
        """)
    query, proj = st.columns(2)
    project_handle = dataiku.api_client().get_project(dataiku.default_project_key())
    vars = project_handle.get_variables()['standard']
    queryType = vars['query_options']

    with query:
        st.title('Choosing Query type')
        input_queryType = st.radio(
            "State how the Query will be done", queryType)

    with proj:
        st.title('Select a Project')
        selected_project = st.selectbox(
            'Project', [config['name'] for config in vars['configuration']])
        st.write(selected_project)
        index = [index for index, project in enumerate(
            vars['configuration']) if selected_project == project['name']][0]
        focusProject = vars['configuration'][index]
        st.write(focusProject)

    st.write('## Displaying the Selected Query Parameters')

    basicData, fuse1, ft1, ws2, ws1 = st.tabs(
        ['Basic Data', 'FUSE1', 'FT1', 'WS2', 'WS1'])

    with fuse1:
        st.table(data=pd.DataFrame(focusProject['FUSE1']))

    with ft1:
        st.table(data=pd.DataFrame(focusProject['FT1']))

    with ws2:
        st.table(data=pd.DataFrame(focusProject['WS2']))

    with ws1:
        st.table(data=pd.DataFrame(focusProject['WS1']))