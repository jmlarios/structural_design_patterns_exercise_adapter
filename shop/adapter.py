
"""Implement the Adapter(s) so our app can speak to 3rd-party SDKs.

Goal: Make StripeAPI and PayPalClient usable via the PaymentProcessor interface without
changing the app code in app.checkout.
"""
from .payments import PaymentProcessor
from .third_party_providers import StripeAPI, PayPalClient

class StripeAdapter(PaymentProcessor):
    """Adapt StripeAPI(charge amount_cents) -> dict to PaymentProcessor(pay amount_eur) -> str."""
    def __init__(self, client: StripeAPI):
        self.client = client

    def pay(self, amount: float) -> str:
        # TODO:
        amount_cents = int(amount * 100)
        self.client.charge(amount_cents)
        merchant_id = self.client.merchant_id
        return "paid {:.2f} EUR via Stripe ({})".format(amount, merchant_id)

class PayPalAdapter(PaymentProcessor):
    """Adapt PayPalClient(make_payment total: float) -> (bool, total) to PaymentProcessor interface."""
    def __init__(self, client: PayPalClient):
        self.client = client

    def pay(self, amount: float) -> str:
        # TODO:
        self.client.make_payment(amount)
        account_email = self.client.account_email
        return "paid {:.2f} EUR via PayPal ({})".format(amount, account_email)
        # - Call self.client.make_payment(amount)
        # - Validate the success flag
        # - Return: "paid 12.34 EUR via PayPal (merchant@example.com)"
        raise NotImplementedError
