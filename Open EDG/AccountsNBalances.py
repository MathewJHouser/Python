class AccountException(Exception):
    pass

class Account:
    def __init__(self, ID_Number):
        self.__number = ID_Number
        self.__funds = 0

    @property
    def balance(self):
        return self.__funds

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise AccountException("Funds cannot be negative. ")
        if abs(self.__funds - amount) > 100000:
            print("Large transactions will be audited. ")
        self.__funds = amount

    @balance.deleter
    def balance(self):
        if self.__funds != 0:
            print("Please withdraw all funds before terminating the account. ")
        else:
            self.__funds = None

    @property
    def ID(self):
        return self.__number

    @ID.setter
    def ID(self, value):
        raise AccountException("You do not have permission to edit account ID numbers. ")

    @ID.deleter
    def ID(self):
        raise AccountException("You do not have permission to delete account ID numbers. ")

    def __str__(self):
        return "Account #{} has a balance of ${}. ".format(self.__number, self.__funds)

account = Account('34-6514-7654-9999-0002')
account.balance += 1000
print(account)

try:
    account.balance = -200
except AccountException as e:
    print('Exception detected:', e)

try:
    account.ID = 'a new one'
except AccountException as e:
    print('Exception detected:', e)

try:
    account.balance += 1_000_000
except AccountException as e:
    print('Exception detected:', e)

try:
    del account.balance
except AccountException as e:
    print('Exception detected:', e)
