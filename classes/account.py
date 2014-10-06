class Account:
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
	self.last_name = last_name
	self.balance = balance

    def withdraw(self, withdrawal_amount):
	self.balance = self.balance - withdrawal_amount	
