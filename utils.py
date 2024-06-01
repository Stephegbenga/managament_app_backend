from datetime import datetime
from models import Products

def timestamp():
    return datetime.utcnow().isoformat()



def next_number_formatted(number_str):
    fixed_length = 5
    # Convert input string to integer and increment it by 1
    next_number = int(number_str) + 1
    # Format the incremented number as a string with leading zeros, fixed length
    formatted_next_number = f'{next_number:0{fixed_length}d}'

    return formatted_next_number


def get_next_product_no(number="auto"):
    # Find the product with the highest product_no
    if number == "auto":
        highest_product = Products.find_one(sort=[("product_no", -1)])
        if highest_product:
            next_product_no = next_number_formatted(highest_product['product_no'])
        else:
            next_product_no = "00001"
    else:
        next_product_no = next_number_formatted(number)

    return next_product_no


