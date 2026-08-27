from typing import Any


class PaymentGateway:
    def charge(self, amount, currency="USD") -> dict[str, Any]:
        raise NotImplementedError("real HTTP here")


gateway = PaymentGateway()


def pay_order(amount, gateway=gateway):
    if amount <= 0:
        raise ValueError("amount must be > 0")
    result = gateway.charge(amount)
    if not result.get("ok"):
        raise RuntimeError("payment failed")
    return result["id"]
