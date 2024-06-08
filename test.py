from models import Products
from utils import timestamp

products = list(Products.find({}))
host_url = 'https://mail.kabuyu-fast.com'
for product in products:
    if product['name'] == "ANA5/2024" and not product.get("is_sold"):
        print(product)
        break

    if product.get("is_sold"):
        print(product)