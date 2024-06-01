from models import Products
from utils import timestamp

products = list(Products.find({}))

for product in products:
    file_url = product['file_url']
    print(file_url)