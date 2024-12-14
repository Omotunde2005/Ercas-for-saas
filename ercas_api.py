import requests
import os
from dotenv import load_dotenv 



load_dotenv()


class ErcasPayClient:
    def __init__(self):   
        """
        
        This client uses the sandbox URL to allow for testing. Visit the ercaspay developer docs @ [https://docs.ercaspay.com] to get the live URL. 
        Get your test token @ [https://sandox.ercaspay.com]
        Get your live token by signing up on the ercaspay website @ [https://ercaspay.com]
        
        """ 

        self.base_url = "https://api.merchant.staging.ercaspay.com/api/v1"
        self.token = os.environ.get("ERCASPAY_SECRET_TOKEN")
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

    def initiate_payment(self, **kwargs):
        payload = {
            "amount": kwargs.get("amount"),
            "paymentReference": "",
            "paymentMethods": "",
            "customerName": "",
            "customerEmail": "",
            "customerPhoneNumber": "",
            "currency": "",
            "feeBearer": "",
            "redirectUrl": "",
            "description": "",
            "metadata": ""
        }

        response = requests.post(f"{self.base_url}/payment/initiate", headers=self.headers, json=payload)
        return response

    def verify_transaction(self, ref):
        pass


