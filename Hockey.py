from bs4 import BeautifulSoup
import streamlit as st
import requests


url = requests.get('https://www.scrapethissite.com/pages/forms/?page_num=1').text
html_template = BeautifulSoup(url, 'lxml')

st.title("Hockey Teams")


table_data = html_template.find('table', class_='table')
table_rows = table_data.find_all('tr')[1:] 

for row in table_rows:
    st.text(row)