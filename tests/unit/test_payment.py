from decimal import Decimal

import pytest

from shop import payment

# mocks


def test_pay_order_success(monkeypatch):  # method style mocking
    def fake_charge(amount, currency="USD"):
        return {"ok": True, "id": "pay_1"}

    monkeypatch.setattr("shop.payment.gateway.charge", fake_charge)
    assert payment.pay_order(Decimal("10.00")) == "pay_1"


def test_pay_order_calls_charge(mocker):  # object style mocking
    fake = mocker.patch(
        "shop.payment.gateway.charge", return_value={"ok": True, "id": "pay_1"}
    )

    payment.pay_order(Decimal("10.00"))

    fake.assert_called_once_with(Decimal("10.00"))


def test_pay_order_failure(mocker):
    fake = mocker.patch("shop.payment.gateway.charge", return_value={"ok": False})

    with pytest.raises(RuntimeError):
        payment.pay_order(Decimal("10.00"))


def test_pay_order_rejects_zero():
    with pytest.raises(ValueError):
        payment.pay_order(0)
