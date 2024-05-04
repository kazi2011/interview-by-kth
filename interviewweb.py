import streamlit as st
import pandas as pd

st.set_page_config(page_title="Interview",page_icon=":tada:",layout="wide")


st.subheader("Hi, I am K.T.Huda :wave:")
st.title("And I want to take your interview")


name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father's name: ")
adr = st.text_area("Enter your address: ")
classd=st.selectbox("Enter your class: ",(1,2,3,4,5,6,7,8,9,10,11,12,))
ac=st.text_input("Enter your fav anime/cartoon ")

button = st.button("Done")
if button :
    st.markdown(f"""Name :{name}
    Father name : {fname}
    address :{adr}
    class : {classd}
    Fav anime/cartoon:""")
    