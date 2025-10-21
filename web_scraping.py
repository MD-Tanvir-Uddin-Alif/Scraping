from bs4 import BeautifulSoup
import requests

base_url = "https://webscraper.io/test-sites/e-commerce/static"

category = input("Enter category (e.g., computers, phones): ").strip().lower()
if not category:
    category = "computers"

subcategory = input("Enter subcategory (e.g., laptops, tablets) [Optional]: ").strip().lower()

if subcategory:
    url = f"{base_url}/{category}/{subcategory}"
else:
    url = f"{base_url}/{category}" if category else base_url

html_template = requests.get(url).text 

soup = BeautifulSoup(html_template, 'lxml')

products = soup.find_all('div', class_='product-wrapper card-body')

for product in products:
    product_image = product.img['src']
    product_descriptio = product.find('div', class_='caption')
    product_name = product_descriptio.find('a', class_='title').text.strip()
    product_price = product_descriptio.h4.span.text
    product_reviews = product.find('div', class_='ratings')
    product_ratting = product_reviews.p.span.text
    product_details = product_descriptio.find('a',class_='title')['href']
    
    print('--------------------------info-------------------------')
    print(f'Product Image:   {product_image}')
    print(f'Product Name:   {product_name}')
    print(f'Product price:   {product_price}')
    print(f'Product rating:   {product_ratting}')
    print(f'Product details:   {product_details}')
