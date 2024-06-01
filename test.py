from models import Product_names

from pprint import pprint
product_names = list(Product_names.find({}, {"_id":0}))

pprint(product_names)