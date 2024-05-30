product_names = [
    'ANA5/2024', 'ANA12/2024', 'JAL6/2024', 'JAL12/2024', 'JR', 'PEACH4/2024', 'JetStar 7/2024'
  ]

from models import Products, Product_names

Product_names.delete_many({})

for name in product_names:
    Product_names.insert_one({"name": name})
    print(name)

print("Done inserting all names")