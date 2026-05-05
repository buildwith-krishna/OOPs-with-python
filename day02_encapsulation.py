class BankAccount():
    def __init__(self):
        self.__balance = 0
    
    def get_balance(self):
        if self.__balance == 0:
            print("Balance is Zero.")
        else:
            print(f"\nBalance : {self.__balance}")

    def set_balance(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit: {amount}. New balance: {self.__balance}")

        else:
            print("Amount should be greater than 0!")


    
bank = BankAccount()
bank.get_balance()

try:
    amount = int(input("Enter amount: ").strip())
    bank.set_balance(amount)
except ValueError:
    print("Enter numbers only!")

