import streamlit as st
import gspread

st.title('My Wholesome Data Capture Project')
st.write("My app wants to collect data from you about...")
st.subheader('Add a new item') 
name = st.text_input('Enter the item name')

def save_into_csv(name, author, link, pair, summ):    
    gc = gspread.service_account(filename='credentials.json')     
    sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1slrPae8iU_yZqS1gWvzxjkMSY7g_UeYP4isYtItbQbo/edit?usp=sharing')    
    worksheet = sh.get_worksheet(0)
