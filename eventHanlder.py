from dataModel import AST
import streamlit as st

def handle_value_change(event, metadata, key: str, index: int = 0): 

  print(event)
  print(metadata)
  print(key)
  print("this is changing the state")
  print(st.session_state[key])
  if event == "governance_projectType":
        AST.SDC_governance_projecType = st.session_state[key]

