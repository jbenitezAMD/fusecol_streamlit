import dataiku
import streamlit as st
import pandas as pd 

def initializeValidationPoint(): 
    return {'QuerySummary' : False,'QueryType' : False,}

def initializeOutput(): 
    return {'QuerySummary': '','QueryType': '', 'TimeFrame' : '',}


validationPoints = initializeValidationPoint()

def submit_QueryPoints(focusProject, selectedQueryType): 
    submitQuerPoint_column, submitQueryType_column = st.columns(2)
    output = initializeOutput()
    st.write('## Validate and Submit Selected Query Parameters')
    validation_Form_FuseCOL(submitQuerPoint_column, 'QuerySummary', 'Validate Query Points', '## Submit Query Status', summary_QueryPoints, focusProject, validationPoints)
    if selectedQueryType != '..': 
        validation_Form_FuseCOL(submitQueryType_column, 'QueryType', 'Validate Query Type', '## Submit Query Type', summary_QueryType, selectedQueryType, validationPoints)

    if validationPoints['QuerySummary'] == True and validationPoints['QueryType'] == True: 
        validateButton = st.sidebar.button('Submit Button', key='SubmitQuery')
        st.write(validateButton)
        if validateButton: 
            output['QuerySummary'] = focusProject
            output['QueryType'] = selectedQueryType
            output['TimeFrame'] = 'Today'
        else: 
            st.write('Hello')
            output = initializeOutput()

    st.write(validationPoints)
    st.write(output)

def summary_QueryPoints(project): 
    with st.expander('Query Points'): 
        textPoints = ['Collected Matching Points', 'FUSE1', 'FT1', 'WS2', 'WS1']
        st.write(f'## {textPoints[0]}')
        st.dataframe(data=project['onlyPrint'], hide_index=True, use_container_width=True)
        st.write(f'## {textPoints[1]}')
        st.dataframe(data=pd.DataFrame(project['FUSE1']), hide_index = True, use_container_width = True)
        st.write(f'## {textPoints[2]}')
        st.dataframe(data=pd.DataFrame(project['FT1']), hide_index = True, use_container_width = True)
        st.write(f'## {textPoints[3]}')
        st.dataframe(data=pd.DataFrame(project['WS2']), hide_index = True, use_container_width = True)
        st.write(f'## {textPoints[4]}')
        st.dataframe(data=pd.DataFrame(project['WS1']), hide_index = True, use_container_width = True)
def summary_QueryType(selectedQueryType): 
    st.write(selectedQueryType)

def validation_Form_FuseCOL(columnName, validationCheck, formTitle, sidebarTitle, function, project, validationPoints): 
    if validationPoints[validationCheck]: valstate = 'complete'
    else: valstate = 'error'
    validated_testSummary = st.sidebar.status(sidebarTitle, state=valstate)
    with columnName:
        st.write(formTitle)
        function(project)
        col1, col2 = st.columns(2)
        with col1: validated_summary = st.button(f'Approve {validationCheck}')
        with col2: unvalidate_summmary = st.button(f'Unapprove {validationCheck}')
        if validated_summary: 
            validationPoints[validationCheck] = True
            validated_testSummary.update(state='complete')
        elif validated_summary == False and unvalidate_summmary == True: 
            validationPoints[validationCheck] = False
            validated_testSummary.update(state='error')
        # if unvalidate_summmary: 
        #     validationPoints[validationCheck] = False
        #     validated_testSummary.update(state='error')