from bs4 import BeautifulSoup
import streamlit as st
import requests

st.title("Hockey Teams")

for i in range(1,25):
    st.error(f"Page no {i}")

    url = f'https://www.scrapethissite.com/pages/forms/?page_num={i}'
    response = requests.get(url)
    html_template = BeautifulSoup(response.text, 'lxml')

    table_data = html_template.find('table', class_='table')
    table_rows = table_data.find_all('tr')[1:] 

    for i, row in enumerate(table_rows, start=1):
        st.warning(f"Team {i}")

        team_name = row.find('td', class_='name').text.strip() if row.find('td', class_='name') else 'N/A'
        team_year = row.find('td', class_='year').text.strip() if row.find('td', class_='year') else 'N/A'
        team_wins = row.find('td', class_='wins').text.strip() if row.find('td', class_='wins') else 'N/A'
        team_losses = row.find('td', class_='losses').text.strip() if row.find('td', class_='losses') else 'N/A'
        team_ot_losses = row.find('td', class_='ot-losses').text.strip() if row.find('td', class_='ot-losses') else 'N/A'

        team_pct_tag = row.find('td', class_='pct text-success') or row.find('td', class_='pct text-danger')
        team_Pct = team_pct_tag.text.strip() if team_pct_tag else 'N/A'

        team_gf = row.find('td', class_='gf').text.strip() if row.find('td', class_='gf') else 'N/A'

        team_diff_tag = row.find('td', class_='diff text-success') or row.find('td', class_='diff text-danger')
        team_diff = team_diff_tag.text.strip() if team_diff_tag else 'N/A'

        st.info(f"{team_name} | Year: {team_year} | Wins: {team_wins} | Losses: {team_losses} | "
                f"OT Losses: {team_ot_losses} | Pct: {team_Pct} | GF: {team_gf} | Diff: {team_diff}")
