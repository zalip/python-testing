from dataclasses import dataclass, field
from decimal import Decimal

from shop.pricing import apply_discount, total


@dataclass
class CartItem:
    sku: str
    price: Decimal
    qty: int = 1

    def __post_init__(self) -> None:
        if self.qty < 1:
            raise ValueError("qty must be >= 1")
        if self.price < 0:
            raise ValueError("price must be >= 0")

    @property
    def line_total(self) -> Decimal:
        return self.price * self.qty


@dataclass
class Cart:
    items: list[CartItem] = field(default_factory=list)
    discount_percent: Decimal = Decimal("0")

    def add(self, item: CartItem) -> None:
        self.items.append(item)

    def subtotal(self) -> Decimal:
        return total([i.line_total for i in self.items])

    def grand_total(self) -> Decimal:
        return apply_discount(self.subtotal(), self.discount_percent)