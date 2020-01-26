# in the_bank.py
class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.id = self.ID_COUNT
        self.name = name
        self.__dict__.update(kwargs)
        if hasattr(self, 'value'):
            self.value = 0
        Account.ID_COUNT += 1

    def transfer(self, amount):
        self.value += amount

class Bank(object):
    def __init__(self):
        super().__init__(id 
        self.account = []

    def checking
    """
    Security means checking if the Account is:
• the right object
• that it is not corrupted
• and that it has enough money
How do we define if a bank account is corrupted?
It has an even number of attributes.
It has an attribute starting with b.
It has no attribute starting with zip or addr.
It has no attribute name, id and value.
P

A transaction is invalid if amount < 0 or if the amount is larger than the funds the first
account has available for transfer.
    """