import dataiku
import streamlit as st
import pandas as pd 

saveState = {
    'OPN': '',
    'LotID': '',
    'KDF' : '',
    'QueryID' : '',
    'LocalCSV' : '',
    'LocalKDF' : '',
}

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

    query_return_value = {
        'OPN': selected_opn,
        'LotID': selcted_LotID,
        'KDF' : selcted_KDF,
        'QueryID' : selcted_QueryID,
        'LocalCSV' :  selcted_LocalCSV,
        'LocalKDF' : selcted_localKDF,
    }

    selected_QueryType = query_return_value[input_queryType]()

    return focusProject, selected_QueryType

def selected_opn(): 
    opn, configID = st.columns(2)
    with opn: 
        opn = st.text_input('Input OPN', value=saveState['OPN'].split('.')[0])
    with configID: 
        try: 
            cfigID = st.text_input('Input ConfigID', value=saveState['OPN'].split('.')[1])
        except IndexError: 
            cfigID = st.text_input('Input ConfigID')
    saveState['OPN'] = opn + '.' + cfigID + '.'
    return saveState['OPN']

def selcted_LotID(): 
    saveState['LotID'] = st.text_input('Input LotID', value=saveState['LotID'])
    return saveState['LotID']

def selcted_KDF(): 
    saveState['KDF'] = st.text_input('Input KDF', value=saveState['KDF'])
    return saveState['KDF']

def selcted_QueryID(): 
    saveState['QueryID'] = st.text_input('Input QueryID', value=saveState['QueryID'])
    return saveState['QueryID']

def selcted_LocalCSV(): 
    uploadCSV = st.file_uploader('Input LocalCSV', )
    if uploadCSV is not None:
        saveState['LocalCSV'] = pd.read_csv(uploaded_file)
    return saveState['LocalCSV']

def selcted_localKDF(): 
    uploadKDF = st.file_uploader('Input LocalKDF', )
    if uploadKDF is not None:
        saveState['LocalKDF'] = uploadKDF.getvalue()
    return saveState['LocalKDF']