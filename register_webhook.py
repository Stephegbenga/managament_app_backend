import requests
import json

# Shopify store credentials


# Webhook details
WEBHOOK_ADDRESS_BASE = 'https://c08d-102-88-69-197.ngrok-free.app'

# Topics you want to create webhooks for
WEBHOOK_TOPICS = {'orders-create': 'orders/create', 'products-update': 'products/update', 'products-create': 'products/create'}


def create_webhook(topic, address):
    url = f"{STORE_URL}/admin/api/2024-04/webhooks.json"
    payload = {"webhook": {"address": address, "topic": topic, "format": "json"}}
    headers = {"X-Shopify-Access-Token": ACCESS_TOKEN, "Content-Type": "application/json"}

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 201:
        print(response.json())
        print(f"Successfully created webhook for topic: {topic}")
    else:
        print(f"Failed to create webhook for topic: {topic}")
        print("Status Code:", response.status_code)
        print("Response:", response.json())


def main():
    for path, topic in WEBHOOK_TOPICS.items():
        print(f"Path-{path}  topic-{topic}")
        address = f"{WEBHOOK_ADDRESS_BASE}/{path}"
        print(f"Creating webhook for topic: {topic} at address: {address}")
        create_webhook(topic, address)


if __name__ == '__main__':
    main()
