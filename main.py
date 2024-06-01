import os, json
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
    return {"status":"success", "data": product_names}


def upload_file(file_name, file):
    try:
        Files.insert_one({'filename': file_name, 'file': file.read()})
        file_url = f"{host_url}/{file_name}"
        return file_url
    except Exception as e:
        pass


@app.post('/product')
def add_new_product():
    try:
        files = request.files.getlist('files')
        req = request.form.get('data')

        # Parse the JSON data
        req = json.loads(req) if req else {}
        all_products = []

        next_product_no = get_next_product_no()
        req['registration_date'] = timestamp()
        for file in files:
            data = req.copy()
            filename = f'{next_product_no}.pdf'
            file_url = upload_file(filename, file)
            data['is_sold'] = False
            data['product_no'] = next_product_no
            data['file_url'] = file_url
            next_product_no = get_next_product_no(next_product_no)
            all_products.append(data)

        Products.insert_many(all_products)
        return {"status":"success", "message":"products uploaded"}
    except Exception as e:
        print(e)
        return {"status":"error", "message":"Internal server error"}, 500



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



@app.route('/files/<filename>')
def get_file(filename):
    file = Files.find_one({'filename': filename})
    if not file:
        return "File does not exist", 404

    file_data = BytesIO(file['file'])
    return send_file(file_data, download_name=filename, mimetype="application/pdf", as_attachment=True)





# shopify webhook events
@app.post('/orders-create')
def orders_create():
    req = request.json
    print(req)
    return {"status":"success"}


@app.post('/orders-update')
def orders_update():
    req = request.json
    print(req)
    return {"status":"success"}


@app.post('/products-create')
def products_create():
    req = request.json
    print(req)
    return {"status":"success"}


@app.post('/products-update')
def products_update():
    req = request.json
    name = req['title']
    price = req['variants'][0]['price']
    Product_names.update_one({"name": name}, {"$set": {"selling_price": price}})
    return {"status":"success"}


if __name__ == '__main__':
    app.run()
