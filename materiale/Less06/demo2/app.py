import numpy as np
import pandas as pd
import streamlit as st
import time
import plotly.express as px

@st.cache
def load_data(n_rows=1000):
    time.sleep(4)  #  make our function super slow
    dataframe = pd.read_csv('iris.csv', nrows=n_rows)
    return dataframe

def main():
    title = st.empty()
    #  define our sidebar title
    st.sidebar.title("Options")
    #  define our sidebar subtitle
    st.sidebar.subheader("Select feature")

    max_rows = st.slider(
                        "Number of observation to show",
                        min_value=20,
                        max_value=50, # should be set automatically 
                        value=23,
                        step=1,
                        )

    # our dataset
    df = load_data(max_rows)
    # show to the user how many records are loaded
    st.write("Records shown: ", df.shape[0])
    # get a list of all numeric columns
    numeric_columns = df.select_dtypes(exclude=object).columns.values
    # create a feature picker
    feature = st.sidebar.selectbox("Click below to select a new feature",numeric_columns)
    # set a proper title
    title.title(feature)
    # Canvas
    fig = px.bar(df[feature])
    #fig = df[feature]
    st.plotly_chart(fig)

if __name__=='__main__':
    main()