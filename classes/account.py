class Account:
    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
	self.last_name = last_name
	self.balance = balance

    def withdraw(self, withdrawal_amount):
	if withdrawal_amount > self.balance:
	    raise Exception 
	self.balance = self.balance - withdrawal_amount

    def get_balance(self):
	return self.balance	
    
    def deposit(self, deposit_amount):
	self.balance = self.balance + deposit_amount	

