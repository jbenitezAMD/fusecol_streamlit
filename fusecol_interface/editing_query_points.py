import dataiku
import streamlit as st
import pandas as pd 

def editing_QuerPoints(focusProject): 
    st.write('## Edit the Selected Query Parameters')

    textPoints = ['Collect Matching', 'FUSE1', 'FT1', 'WS2', 'WS1']
    st.write(f'## {textPoints[0]}')
    collect_matchingPoints = pd.DataFrame({
        'Collect Matching Points': focusProject['onlyPrint'],
        'Enable' : [True for _ in range(len(focusProject['onlyPrint']))],
    })
    collected_MatchingPoints = st.data_editor(collect_matchingPoints, hide_index= True, use_container_width=True)
    focusProject['onlyPrint'] = collected_MatchingPoints[collected_MatchingPoints['Enable'] == True]['Collect Matching Points']

    st.write(f'## {textPoints[1]}')
    focusProject['FUSE1'] = st.data_editor(data=pd.DataFrame(focusProject['FUSE1']), hide_index = True, use_container_width = True)
    st.write(f'## {textPoints[2]}')
    focusProject['FT1'] = st.data_editor(data=pd.DataFrame(focusProject['FT1']), hide_index = True, use_container_width = True)
    st.write(f'## {textPoints[3]}')
    focusProject['WS2'] = st.data_editor(data=pd.DataFrame(focusProject['WS2']), hide_index = True, use_container_width = True)
    st.write(f'## {textPoints[4]}')
    focusProject['WS1'] = st.data_editor(data=pd.DataFrame(focusProject['WS1']), hide_index = True, use_container_width = True)
