import streamlit as st
from bs4 import BeautifulSoup
import requests

st.title("Web Scraper E-commerce Products")

url = st.text_input(
    "Select Product Category",
    "https://webscraper.io/test-sites/e-commerce/allinone"
)

if st.button("Scrape Now"):

    try:
        html_template = requests.get(url).text
        soup = BeautifulSoup(html_template, 'lxml')

        products = soup.find_all('div', class_='product-wrapper card-body')

        if not products:
            st.warning("No products found! Check the URL.")
        else:
            for product in products:
                product_image = product.img['src']
                product_descriptio = product.find('div', class_='caption')
                product_name = product_descriptio.find('a', class_='title').text.strip()
                product_price = product_descriptio.h4.span.text
                product_reviews = product.find('div', class_='ratings')
                product_ratting = product_reviews.p.span.text
                product_details = product_descriptio.find('a',class_='title')['href']

                st.write("###Product Found")
                st.image("https://webscraper.io" + product_image)
                st.write(f"**Name:** {product_name}")
                st.write(f"**Price:** {product_price}")
                st.write(f"**Rating:** {product_ratting}")
                st.write(f"**Details Link:** https://webscraper.io{product_details}")
                st.markdown("---")

    except Exception as e:
        st.error(f"Error: {e}")
