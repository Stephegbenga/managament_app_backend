from models import Products
from utils import timestamp


Products.update_one({}, {"$set": {"sold_date": timestamp(), "is_sold": True}})
