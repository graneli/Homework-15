class Person:
    def __init__(self, name, deposit=1000, loan=0):
        self.name = name
        self.deposit = deposit
        self.loan = loan

    def __str__(self):
        return f"Person(Name: {self.name}, Deposit: {self.deposit}, Loan: {self.loan})"

class House:
    def __init__(self, ID, price, owner):
        self.ID = ID
        self.price = price
        self.owner = owner
        self.status = "for sale"

    def sell(self, buyer, loan_amount=0):
        if loan_amount > 0:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold with a loan"
            buyer.loan += loan_amount
            print(f"Apartment sold to {buyer.name} with a loan of {loan_amount}. New status: {self.status}.")
        else:
            self.owner.deposit += self.price
            self.owner = buyer
            self.status = "sold"
            print(f"Apartment sold to {buyer.name}. New status: {self.status}.")

seller = Person("Natia")
buyer = Person("TaTia")

apartment = House(ID="123", price=50000, owner=seller)

apartment.sell(buyer)

apartment.sell(buyer, loan_amount=20000)