import streamlit as st
from bs4 import BeautifulSoup
import requests

st.title("Web Scraper — E-commerce Products")

base_url = "https://webscraper.io/test-sites/e-commerce/static"

category = st.text_input("Enter category (e.g., computers, phones)", "computers").strip().lower()
subcategory = st.text_input("Enter subcategory (e.g., laptops, tablets) [Optional]").strip().lower()

if st.button("Scrape Now"):
    if subcategory:
        url = f"{base_url}/{category}/{subcategory}"
    else:
        url = f"{base_url}/{category}"

    st.write(f" Scraping URL: {url}")

    try:
        html_template = requests.get(url).text
        soup = BeautifulSoup(html_template, 'lxml')

        products = soup.find_all('div', class_='product-wrapper card-body')

        if not products:
            st.warning("No products found. Try a different category or subcategory.")

        for product in products:
            product_image = product.img['src']
            product_descriptio = product.find('div', class_='caption')
            product_name = product_descriptio.find('a', class_='title').text.strip()
            product_price = product_descriptio.h4.span.text
            product_reviews = product.find('div', class_='ratings')
            product_ratting = product_reviews.p.span.text
            product_details = product_descriptio.find('a',class_='title')['href']

            st.write("----")
            st.image("https://webscraper.io" + product_image)
            st.write(f"**Name:** {product_name}")
            st.write(f"Price: {product_price}")
            st.write(f"Rating: {product_ratting}")
            st.write(f"Details: https://webscraper.io{product_details}")

    except Exception as e:
        st.error(f"Error: {e}")
