
import pytest
from shop.app import checkout
from shop.adapter import StripeAdapter, PayPalAdapter
from shop.third_party_providers import StripeAPI, PayPalClient

@pytest.mark.parametrize("amount", [0.01, 12.34, 1000.00])
def test_checkout_with_stripe_adapter(amount):
    adapter = StripeAdapter(StripeAPI(merchant_id="acct_TEST"))
    # Implementations should format to 2 decimals.
    receipt = checkout(adapter, amount)
    assert receipt == f"paid {amount:.2f} EUR via Stripe (acct_TEST)"

@pytest.mark.parametrize("amount", [0.01, 19.99, 250.50])
def test_checkout_with_paypal_adapter(amount):
    adapter = PayPalAdapter(PayPalClient(account_email="seller@test.com"))
    receipt = checkout(adapter, amount)
    assert receipt == f"paid {amount:.2f} EUR via PayPal (seller@test.com)"

def test_negative_amount_raises():
    adapter = StripeAdapter(StripeAPI())
    with pytest.raises(ValueError):
        checkout(adapter, -1)

def test_zero_amount_raises():
    adapter = PayPalAdapter(PayPalClient())
    with pytest.raises(ValueError):
        checkout(adapter, 0)
