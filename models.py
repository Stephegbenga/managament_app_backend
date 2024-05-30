from dotenv import load_dotenv
load_dotenv()
from pymongo import MongoClient
import os

DB_URL=os.environ.get('database_url')

conn = MongoClient(DB_URL)
db = conn.get_database("main_db")

Files = db.get_collection("files")
Products = db.get_collection("products")
Product_names = db.get_collection("product_names")

# write a simple function

