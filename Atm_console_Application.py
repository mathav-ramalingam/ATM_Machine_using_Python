class Cardholder:
    def __init__(self, Ac_no, pin, name, balance):
        self.Ac_no = Ac_no
        self.pin = pin
        self.name = name
        self.balance = balance
        self.transactions = []

    def menu(self):
        print("1. Transaction History")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Transfer")
        print("5. Balance")
        print("6. Quit")

    def check_balance(current_user):
        print("Your current balance is: ", current_user.balance)
        print("--------------------------------")

    def deposit(self, current_user):
        self.balance += amount
        self.transactions.append(f"Deposit:   +{amount}")

    def withdraw(self, current_user):
        if self.balance >= amount:
            self.balance -= amount
            self.transactions.append(f"Withdrawal: -{amount}")
        else:
            print("Insufficient funds")

    def transfer(self, user_id, user_name, amount):
        if self.balance >= amount:
            self.balance -= amount
            print("------------------------------------------------------------------------")
            print(f"Amount Transfer to {user_name} & Account Number is {user_id} : +{amount} ")
            print("------------------------------------------------------------------------")
            self.transactions.append(f"Amount Transfer: -{amount}")
        else:
            print("Insufficient funds")

    def transaction_history(self):
        print("--------------------------")
        for transaction in self.transactions:
            print(transaction)
        print("--------------------------")




if __name__ == "__main__":
    current_user = Cardholder("","","","")

    list_of_user = []

# Creating instances of Cardholder class and appending to list_of_user
    list_of_user.append(Cardholder("1234567891012131",1608,"Mathav",2000))
    list_of_user.append(Cardholder("1112131415161718",1974,"Ram",5000))
    list_of_user.append(Cardholder("2021222324252627",2104,"Sam",1800))


# User input to enter debit card number and validate it
    debitcardnum = " "
    while True:
        try:
            debitcardnum = input("Enter the Debit card Number: ")
            debitmatch = [i for i in list_of_user if i.Ac_no == debitcardnum]
            current_user = debitmatch[0]
            break
        except:
            print("Card number not recognized. Please try again.")


# User input to enter PIN and validate it
    while True:
        try:
            pin = int(input("Enter the Pin: "))
            if(current_user.pin == pin):
                break
            else:
                print("Invalid Pin. Please try again. ")
        except:
            print("Invalid Pin. Please try again. ")


# Greeting the user
    print("=============================================")
    print("Welcome ", current_user.name, " :)")
    print("=============================================")


# Main menu for the ATM functionality
    while True:
            current_user.menu()
            choice = input("Enter choice: ")

            if choice == "1":
                current_user.transaction_history()

            elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                current_user.withdraw(amount)

            elif choice == "3":
                amount = float(input("Enter amount to deposit: "))
                current_user.deposit(amount)

            elif choice == "4":
                user_id = input("Enter the Account Number : ")
                user_name = input("Enter the Account Holder Name: ")
                amount = float(input("Enter amount to transfer: "))
                current_user.transfer(user_id,user_name, amount)
            
            elif choice == "5":
                current_user.check_balance()

            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")