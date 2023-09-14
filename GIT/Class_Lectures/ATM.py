import time
balance = 45000
password = "1234"


def bal():
    global balance
    print("Your current balance is ", balance,"\n")


def withdraw(amount):
    global balance
    balance = balance - amount if amount <= balance else print("Insufficient balance")


def deposit(amount):
    global balance
    balance = balance + amount


def loan(amount):
    global balance
    balance = balance + amount


if __name__ == "__main__":
    while True:
        print("Welcome to ATM".center(50, "-"))
        if input("Enter The Card :").lower() == "card":
            if input("Enter the Pin : ") == password:
                print("1. Withdraw")
                print("2. Deposit")
                print("3. Loan")
                print("4. Exit")
                ch = int(input("Enter your choice : "))
                if ch == 1:
                    amount = int(input("Enter the amount to withdraw : "))
                    withdraw(amount)
                    bal()
                elif ch == 2:
                    amount = int(input("Enter the amount to deposit : "))
                    deposit(amount)
                    bal()
                elif ch == 3:
                    amount = int(input("Enter the amount to loan : "))
                    loan(amount)
                    bal()
                elif ch == 4:
                    print("Thank you for using ATM".center(50, "-"))
                    break
                else:
                    print("Plz Enter a Valid Choice")
            else:
                print("Plz Enter a Valid Pin")
        else:
            print("Plz Enter a Valid Card")
        time.sleep(3)
