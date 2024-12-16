import reflex as rx
from datetime import datetime, timedelta
from .base import State
from login_test.ercas_api import ErcasPayClient
from urllib.parse import urljoin
from sqlmodel import select
from login_test.models import User, Subscription

class AppState(State):
    currency: str

    @rx.event
    def change_value(self, value):
        self.currency = value

    @rx.var
    def get_redirect_url(self) -> str:
        url = self.router.page.full_raw_path
        base_url = urljoin(url, "/")
        redirect_url = base_url + "verify/payment"
        return redirect_url

    def _make_payment(self, usd_amount, ngn_amount, plan):
        if self.currency == "NGN":
            amount = ngn_amount

        client = ErcasPayClient()
        payload = {
            "amount":amount,
            "customerName": self.user.username,
            "customerEmail": self.user.email,
            "currency": self.currency,
            "redirectUrl": self.get_redirect_url,
            "description":"a test payment",
            "metadata": {
                "plan": plan
            }
        }
        try:
            response = client.initiate_payment(payload)
        except Exception as e:
            print(e)
            return False
        else:
            return response
        
    
    def handle_payment(self, usd_amount, ngn_amount, plan):
        response = self._make_payment(usd_amount, ngn_amount, plan)

        if response:
            if response["requestSuccessful"]:
                checkout_url = response["responseBody"]["checkoutUrl"]
                return rx.redirect(checkout_url)
            

    @rx.var
    def _get_tranasaction_metadata(self) -> dict:
        ref_number = self.router.params.get("transactionReference", None)
        client = ErcasPayClient()

        try:
            response = client.verify_transaction(ref_number)
        except Exception as e:
            print(e)
        else:
            if response["requestSuccessful"]:
                responseBody = response["responseBody"]
                if responseBody["status"] == "SUCCESSFUL":
                    return {
                        "ref": ref_number,
                        "amount": responseBody["amount"],
                        "plan": responseBody["metadata"]["plan"] 
                    }


    @rx.var
    def has_query_params(self) -> bool:
        transactionref = self.router.params.get("transactionReference", None)
        if transactionref:
            return True
        return False

    def ref_in_db(self, ref_number) -> bool:
        with rx.session() as session:
            if session.exec(select(Subscription).where(Subscription.ref_number == ref_number)).first():
                return True
            return False

    def new_subscription(self, metadata):
        with rx.session() as session:
            # VERIFY SUBSCRIPTION
            start = datetime.now()
            expiry_date = start + timedelta(days=30)
            subscription = Subscription(
                plan=metadata["plan"],
                price=metadata["amount"],
                start=start,
                end=expiry_date,
                ref_number=metadata["ref"],
                user=self.user
            )
            session.add(subscription)
            session.commit()
            return rx.redirect("/dashboard")

    def verify_payment(self):
        if not self.logged_in:
            return rx.redirect("/login")
        
        if not self.has_query_params:
            return rx.redirect("/")
        
        transaction_metadata = self._get_tranasaction_metadata
        
        if self.ref_in_db(transaction_metadata["ref"]):
            return rx.redirect("/dashboard")
        
        self.new_subscription(transaction_metadata)
        return rx.redirect("/dashboard")
        


        


