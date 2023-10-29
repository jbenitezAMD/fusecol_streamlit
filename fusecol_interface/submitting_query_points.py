import dataiku
import streamlit as st
import pandas as pd 

def submit_QueryPoints(focusProject, selectedQueryType): 

    validationPoints = {
        'QuerySummary' : False,
        'QueryType' : False,
    }
    st.write('## Validate and Submit Selected Query Parameters')

    # summary.update('Query Point Validation Complete', state = 'complete')
    # approveButton_Columns, disproveButton_Column = st.columns([1, 2])
    with st.form('Validate Query Points'):
        st.sidebar.write('---\n## Submit Query Status\n')
        validated = st.sidebar.status('Validate Query Points', state='error')
        summary_QueryPoints(focusProject)
        validated_summary = st.form_submit_button('Approve')
        if validated_summary: 
            validationPoints['QuerySummary'] = True
            validated.update(state='complete')
    if selectedQueryType != '..': 
        with st.form('Validate Query Type'): 
            st.sidebar.write('## Submit Query Type\n')
            summary_QueryType(selectedQueryType)
            validated_testQuery = st.sidebar.status('Validate Query Type', state='error')
            validated_query = st.form_submit_button('Approve')
            if validated_query: 
                validationPoints['QueryType'] = True
                validated_testQuery.update(state = 'complete')


def summary_QueryPoints(focusProject): 
    with st.expander('Query Points'): 
        textPoints = ['Collected Matching Points', 'FUSE1', 'FT1', 'WS2', 'WS1']
        st.write(f'## {textPoints[0]}')
        st.dataframe(data=focusProject['onlyPrint'], hide_index=True, use_container_width=True)
        st.write(f'## {textPoints[1]}')
        st.dataframe(data=pd.DataFrame(focusProject['FUSE1']), hide_index = True, use_container_width = True)
        st.write(f'## {textPoints[2]}')
        st.dataframe(data=pd.DataFrame(focusProject['FT1']), hide_index = True, use_container_width = True)
        st.write(f'## {textPoints[3]}')
        st.dataframe(data=pd.DataFrame(focusProject['WS2']), hide_index = True, use_container_width = True)
        st.write(f'## {textPoints[4]}')
        st.dataframe(data=pd.DataFrame(focusProject['WS1']), hide_index = True, use_container_width = True)
def summary_QueryType(selectedQueryType): 
    st.write(selectedQueryType)