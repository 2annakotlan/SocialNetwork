import pandas as pd
import streamlit as st
from googlesheets.py import df

# Display data in Streamlit
st.write("Here is the data:")
st.dataframe(df)

