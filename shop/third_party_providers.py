
class StripeAPI:
    """Pretend this is a 3rd-party SDK with an incompatible interface."""
    def __init__(self, merchant_id: str = "acct_123"):
        self.merchant_id = merchant_id

    def charge(self, amount_cents: int) -> dict:
        # In the real SDK this would hit Stripe's servers.
        # Here we just return a dict payload similar to what a real API might return.
        return {"ok": True, "amount_cents": amount_cents, "merchant_id": self.merchant_id}

class PayPalClient:
    """Another 3rd-party SDK with a different interface."""
    def __init__(self, account_email: str = "merchant@example.com"):
        self.account_email = account_email

    def make_payment(self, total: float) -> tuple:
        # Returns (success, total_paid)
        return (True, float(total))
