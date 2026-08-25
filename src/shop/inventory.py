class OutOfStockError(Exception):
    pass


class Inventory:
    def __init__(self) -> None:
        self._stock: dict[str, int] = {}

    def set_stock(self, sku: str, qty: int) -> None:
        if qty < 0:
            raise ValueError("qty must be >= 0")
        self._stock[sku] = qty

    def available(self, sku: str) -> int:
        return self._stock.get(sku, 0)

    def reserve(self, sku: str, qty: int) -> None:
        if qty < 1:
            raise ValueError("qty must be >= 1")
        have = self.available(sku)
        if have < qty:
            raise OutOfStockError(f"{sku}: need {qty}, have {have}")
        self._stock[sku] = have - qty