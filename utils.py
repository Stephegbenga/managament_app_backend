from datetime import datetime
from models import Products
import requests, base64, os, json
from dotenv import load_dotenv
load_dotenv()


account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")
account_phone_no = os.getenv("account_phone_no")
host_url = os.getenv("host_url")
shopify_token = os.getenv("shopify_token")
STORE_URL = os.getenv("STORE_URL")

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


def send_sms_message(phone_no, text):


    credentials = f"{account_sid}:{auth_token}"

    credentials_bytes = credentials.encode('utf-8')
    base64_credentials = base64.b64encode(credentials_bytes).decode('utf-8')

    url = f"https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json"


    payload = {"To": f"{phone_no}", "From": f"{account_phone_no}", "Body": text}

    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Authorization': f'Basic {base64_credentials}'}

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.json())


def register_webhook():
    WEBHOOK_TOPICS = {'orders-create': 'orders/create', 'products-update': 'products/update', 'products-create': 'products/create'}

    for path, topic in WEBHOOK_TOPICS.items():
        print(f"Path-{path}  topic-{topic}")
        address = f"{host_url}/{path}"
        print(f"Creating webhook for topic: {topic} at address: {address}")

        url = f"{STORE_URL}/admin/api/2024-04/webhooks.json"
        payload = {"webhook": {"address": address, "topic": topic, "format": "json"}}
        headers = {"X-Shopify-Access-Token": shopify_token, "Content-Type": "application/json"}

        response = requests.post(url, data=json.dumps(payload), headers=headers)

        if response.status_code == 201:
            print(response.json())
            print(f"Successfully created webhook for topic: {topic}")
        else:
            print(f"Failed to create webhook for topic: {topic}")
            print("Status Code:", response.status_code)
            print("Response:", response.json())

