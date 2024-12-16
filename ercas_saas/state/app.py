import reflex as rx
from datetime import datetime, timedelta
from .base import State
from ercas_saas.ercas_api import ErcasPayClient
from urllib.parse import urljoin
from sqlmodel import select
from ercas_saas.models import User, Subscription


# The state that manages the app
class AppState(State):
    currency: str
    payment_btn_loading: bool = False

    @rx.event
    def change_value(self, value):
        """ An event handler that sets the user selected currency """
        self.currency = value

    @rx.var
    def _get_redirect_url(self) -> str:
        """ Used to get the redirect url where the user will be redirected to after payment """
        url = self.router.page.full_raw_path
        base_url = urljoin(url, "/")
        redirect_url = base_url + "verify/payment"
        return redirect_url

    def _make_payment(self, usd_amount, ngn_amount, plan):
        """ A function that sends a payment request to the ErcasPay API """
        amount = usd_amount
        if self.currency == "NGN":
            amount = ngn_amount

        client = ErcasPayClient()
        payload = {
            "amount":amount,
            "customerName": self.user.username,
            "customerEmail": self.user.email,
            "currency": self.currency,
            "redirectUrl": self._get_redirect_url,
            "description": "a test payment",
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
        """ An event handler that handles user payments and redirects them to ErcasPay payment link """
        self.payment_btn_loading = True
        response = self._make_payment(usd_amount, ngn_amount, plan)

        if response:
            if response["requestSuccessful"]:
                checkout_url = response["responseBody"]["checkoutUrl"]
                self.payment_btn_loading = False
                return rx.redirect(checkout_url)
            

    def _get_transaction_metadata(self) -> dict:
        """ A backend function that retrieves a transaction metadata from ErcasPay """
        ref_number = self.router.page.params.get("transactionReference", None)
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
        """ A state var that checks if there the transactionReference exists in the query parameters """
        transactionref = self.router.page.params.get("transactionReference", None)
        if transactionref:
            return True
        return False

    def ref_in_db(self, ref_number) -> bool:
        """ This function checks if the tranasactionReference number exists in the database """
        with rx.session() as session:
            if session.exec(select(Subscription).where(Subscription.ref_number == ref_number)).first():
                return True
            return False

    def new_subscription(self, metadata):
        """ A function used to register a new subscription instance to the database """
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
        """ An event handler that verifies a user subscription """
        if not self.logged_in:
            return rx.redirect("/login")
        
        if not self.has_query_params:
            return rx.redirect("/")
        
        transaction_metadata = self._get_transaction_metadata()
        
        if self.ref_in_db(transaction_metadata["ref"]):
            return rx.redirect("/dashboard")
        
        self.new_subscription(transaction_metadata)
        return rx.redirect("/dashboard")
        


        


