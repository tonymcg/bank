#!/usr/bin/python

import unittest2
import account

class ATMOperations(unittest2.TestCase):

    def setUp(self):
        self.balance = 1000
	self.acc = account.Account("Anthony","McGlone",10000)
	f = account.Account("Anthony","McG",10000)
	print f
	f.withdraw(500)

    def test_withdraw_operation(self):
	#self.acc.withraw(500)
	#self.assertEquals(500, self.acc.get_balance())
	l = []

if __name__ == '__main__':
    unittest2.main()
