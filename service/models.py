"""Module containing the Account model"""


class Account:

    """Class representing a Customer Account"""
    data = []
    index = 0

    def __init__(self, name, email, address):
        Account.index += 1
        self.id = Account.index
        self.name = name
        self.email = email
        self.address = address

    def save(self):
        Account.data.append(self)

    @classmethod
    def all(cls):
        return cls.data

    @classmethod
    def find(cls, account_id):
        for account in cls.data:
            if account.id == account_id:
                return account
        return None
