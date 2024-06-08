from models import Products
from utils import timestamp

products = list(Products.find({}))
host_url = 'https://mail.kabuyu-fast.com'
for product in products:
    file_url = product['file_url']
    print(file_url)
    file_name = file_url.split("/")[-1]
    print(file_name)
    new_file_url = f"{host_url}/files/{file_name}"
    Products.update_one({"_id": product['_id']}, {"$set": {"file_url": new_file_url}})
