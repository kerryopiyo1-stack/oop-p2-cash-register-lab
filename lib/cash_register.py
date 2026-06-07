class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.previous_transactions = []

    @property
    def discount(self):
        return self._discount

    @discount.setter
    def discount(self, value):
        if isinstance(value, int) and 0 <= value <= 100:
            self._discount = value
        else:
            print("Not valid discount")
            self._discount = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity

        for _ in range(quantity):
            self.items.append(title)

        self.previous_transactions.append({
            "title": title,
            "price": price,
            "quantity": quantity
        })

    def apply_discount(self):
        if self.discount == 0 or not self.previous_transactions:
            print("There is no discount to apply.")
            return

        self.total = self.total - (self.total * self.discount / 100)

        print(f"After the discount, the total comes to ${int(self.total)}.")

        self.previous_transactions.pop()

    def void_last_transaction(self):
        if not self.previous_transactions:
            self.total = 0.0
            return self.total

        last = self.previous_transactions.pop()

        self.total -= last["price"] * last["quantity"]

        for _ in range(last["quantity"]):
            if last["title"] in self.items:
                self.items.remove(last["title"])

        if not self.items:
            self.total = 0.0

        return self.total