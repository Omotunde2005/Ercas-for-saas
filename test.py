from ercas_saas.ercas_api import ErcasPayClient

client = ErcasPayClient()
payload = {
    "amount": 100,
    "customerName": "Emiloju",
    "customerEmail": "edunrilwan@gmail.com",
    "currency": "NGN",
    "redirectUrl": "http://localhost:3000/",
    "description":"a test payment"
}

response = client.initiate_payment(
    payload
)


print(response)
