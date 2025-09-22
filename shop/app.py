
from .payments import PaymentProcessor

def checkout(processor: PaymentProcessor, basket_total: float) -> str:
    """App code that depends on the PaymentProcessor *target* interface, not concrete gateways."""
    if basket_total <= 0:
        raise ValueError("basket_total must be positive")
    receipt = processor.pay(basket_total)
    return receipt
