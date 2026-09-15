class BankAccount: 
    # TODO: Add class and instance attributes at their appropriate places
    total_accounts = 0
    total_balance = 0
    
    def __init__(self, name: str, balance: int) -> None:
        self.__name = name
        self.__balance = balance
        BankAccount.total_accounts += 1
        BankAccount.total_balance += balance

    def get_balance(self) -> int:
        return self.__balance

    def get_name(self) -> str:
        return self.__name

# TODO: Create two accounts

alice = BankAccount("Alice", 1000)
bob = BankAccount("Bob", 2000)

# TODO: Print the information using the mentioned format

print(f"{alice.get_name()}'s balance: ${alice.get_balance()}")
print(f"{bob.get_name()}'s balance: ${bob.get_balance()}")
print(f"Total Accounts: {BankAccount.total_accounts}")
print(f"Total Balance: ${BankAccount.total_balance}")

