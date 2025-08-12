import streamlit as st 
import pandas as pd 
import numpy as np 

st.title("hello world")

with st.sidebar:
    st.header("About app")
    st.write("This is my first app!")
st.header ("this is a header with divider " , divider='rainbow')
st.markdown("this is created using st.markdown")

x= st.slider("Choose an x value" , 1, 10)
st.write("The value of :blue[***x***] is :" , x)

st.subheader("st.area_chart")
chart_data = pd.DataFrame(np.random.randn(20,3), columns=['a','b','c'])
st.area_chart(chart_data)
