
# Reference solution (not imported by tests)
from shop.payments import PaymentProcessor
from shop.third_party_providers import StripeAPI, PayPalClient

class StripeAdapter(PaymentProcessor):
    def __init__(self, client: StripeAPI):
        self.client = client

    def pay(self, amount: float) -> str:
        cents = int(round(amount * 100))
        payload = self.client.charge(cents)
        merchant_id = payload.get("merchant_id", "unknown")
        return f"paid {amount:.2f} EUR via Stripe ({merchant_id})"

class PayPalAdapter(PaymentProcessor):
    def __init__(self, client: PayPalClient):
        self.client = client

    def pay(self, amount: float) -> str:
        ok, total = self.client.make_payment(amount)
        if not ok:
            raise RuntimeError("PayPal payment failed")
        return f"paid {total:.2f} EUR via PayPal ({self.client.account_email})"
