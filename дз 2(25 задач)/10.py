class BankError(Exception):
    pass
class InvalidAmountError(BankError):
    pass
class InsufficientFundsError(BankError):
    pass
class AccountBlockedError(BankError):
    pass

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Сумма снятия должна быть положительной")
    if balance < amount:
        raise InsufficientFundsError("Недостаточно средств на счёте")
    return balance-amount

balance = int(input())
amount = int(input())
print(withdraw(balance, amount))