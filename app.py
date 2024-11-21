import pandas as pd
import streamlit as st
from googlesheets import df

# Display data in Streamlit
st.write("Here is the data:")
st.dataframe(df)

