import os
from flask import Flask, request, send_file
from models import Files, Products, Product_names
app = Flask(__name__)
from io import BytesIO
from flask_cors import CORS
from dotenv import load_dotenv
from utils import timestamp, get_next_product_no
load_dotenv()

host_url=os.getenv("host_url")

CORS(app)

@app.get("/")
def home():
    return {"status":"success", "message":"online"}


@app.post("/product_name")
def add_new_product_name():
    req = request.json
    name = req['name']
    Product_names.update_one({"name": name}, {"$set": {"name": name}}, upsert=True)
    return {"status":"success", "message": "product added"}


@app.get("/product_name")
def get_product_names():
    product_names = list(Product_names.find({}, {'_id':0}))
    all_product_names = [product_name['name'] for product_name in product_names]
    return {"status":"success", "data": all_product_names}

@app.post('/product')
def add_new_product():
    req = request.json
    req['registration_date'] = timestamp()
    req['product_no'] = get_next_product_no()
    req['is_sold'] = False
    Products.insert_one(req)
    return {"status":"success", "message":"item added"}

@app.get('/product')
def get_product():
    type = request.args.get('type')
    if type == 'sold':
        is_sold = True
    else: # type =exhibition
        is_sold = False

    items = list(Products.find({"is_sold": is_sold}, {"_id": 0}))
    response = {"status":"success", "data": items}
    return response


@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file_name = f"{get_next_product_no()}.pdf"
        file = request.files['file']
        Files.insert_one({'filename': file_name, 'file': file.read()})
        file_url = f"{host_url}/{file_name}"
        return {'status': 'success', 'url': file_url}
    except Exception as e:
        return {'status':'error', 'message':'internal server error'}, 500


@app.route('/files/<filename>')
def get_file(filename):
    file = Files.find_one({'filename': filename})
    if not file:
        return "File does not exist", 404

    file_data = BytesIO(file['file'])
    return send_file(file_data, download_name=filename, mimetype="application/pdf", as_attachment=True)


if __name__ == '__main__':
    app.run()
