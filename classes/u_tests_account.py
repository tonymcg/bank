#!/usr/bin/python

import unittest2
import account

class ATMOperations(unittest2.TestCase):

    def setUp(self):
        self.balance = 1000

    def test_withdraw_operation(self):
	f = account.Account("Anthony","McG",1000)
	f.withdraw(500)
	self.assertEquals(500, f.get_balance())

if __name__ == '__main__':
    unittest2.main()
