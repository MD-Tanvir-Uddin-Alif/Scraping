from bs4 import BeautifulSoup
import streamlit as st
import requests


st.title("Countries of the World")
url = requests.get('https://www.scrapethissite.com/pages/simple/').text

html_template = BeautifulSoup(url, 'lxml')

base_list = html_template.find_all('div', class_='col-md-4 country')


for plist, i in zip(base_list, range(1, len(base_list))):
    st.warning(f"Country{i}")
    country_name = plist.h3.text
    country_info = plist.find('div', class_='country-info')
    city_name = country_info.find('span',class_='country-capital').text
    country_population = country_info.find('span', class_='country-population').text
    country_area = country_info.find('span', class_='country-area').text
    st.info(country_name)
    st.info(city_name)
    st.info(country_population)
    st.info(country_area)




