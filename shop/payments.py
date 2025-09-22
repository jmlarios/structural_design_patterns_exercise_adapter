
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    """Target interface expected by our app."""
    @abstractmethod
    def pay(self, amount: float) -> str:
        """Charge the given amount (in EUR) and return a human-readable receipt string."""
        raise NotImplementedError
