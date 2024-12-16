from urllib.parse import urljoin
from login_test.ercas_api import ErcasPayClient
from dotenv import load_dotenv 
import os


client = ErcasPayClient()
payload = {
    "amount": 100,
    "customerName": "Emiloju",
    "customerEmail": "edunrilwan@gmail.com",
    "currency": "NGN",
    "redirectUrl": "http://localhost:3000/",
    "description":"a test payment"
}

# response = client.initiate_payment(
#     payload
# )


#print(response)
print(client.token)
