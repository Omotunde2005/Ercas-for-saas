import requests
import os
import secrets
import string
from dotenv import load_dotenv 


load_dotenv()


class ErcasPayClient:
    def __init__(self):   
        """
        
        This client uses the sandbox URL to allow for testing the API. Visit the ercaspay developer docs @ [https://docs.ercaspay.com] to get the live URL. 
        Get your test token @ [https://sandox.ercaspay.com]
        Get your live token by signing up on the ercaspay website @ [https://ercaspay.com]
        
        """ 

        self.base_url = "https://api.merchant.staging.ercaspay.com/api/v1"
        self.token = os.environ["ERCASPAY_SECRET_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def generate_reference(self):
        characters = string.ascii_letters
        return ''.join(secrets.choice(characters) for _ in range(12))

    def initiate_payment(self, payload):
        payload["paymentReference"] = self.generate_reference()
        payload["paymentMethods"] = "bank"
        response = requests.post(f"{self.base_url}/payment/initiate", headers=self.headers, json=payload)
        return response.json()

    def verify_transaction(self, ref):
        response = requests.get(f"{self.base_url}/payment/transaction/verify/{ref}", headers=self.headers)
        return response.json()


