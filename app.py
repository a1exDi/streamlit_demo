import streamlit as st
st.title('My Wholesome Data Capture Project')
st.write("My app wants to collect data from you about...")
st.subheader('Add a new item') 
name = st.text_input('Enter the item name')
