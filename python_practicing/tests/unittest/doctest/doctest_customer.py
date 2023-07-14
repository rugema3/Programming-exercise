class Customer:
    """
    A sample customer class
    """
    discount = 0.95

    def __init__(self, first, last, purchase):
        self.first = first
        self.last = last
        self.purchase = purchase

    def customer_mail(self):
        return f'{self.first}.{self.last}@email.com'

    def customer_fullname(self):
        return f'{self.first} {self.last}'

    def apply_discount(self):
        self.purchase = int(self.purchase * self.discount)
        return self.purchase
