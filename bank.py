balance = 0.00 

while True:
    act = input("Would you like to check balance, deposit money, withdraw money, or exit? (check, deposit, withdraw, exit): ")
    #check balance
    if act == "check":
        print(f"Your balance is ${balance}.")
    #deposit money
    elif act == "deposit":
        amount = float(input("How much would you like to deposit? "))
        balance += amount
        print(f"You have deposited ${amount}.")
        print(f"Your balance is ${balance}.")
    #withdraw money
    elif act == "withdraw":
        amountw = float(input("How much would you like to withdraw? "))
        if amountw <= balance:
            balance -= amountw
            print(f"You have withdrawn ${amountw}.")
            print(f"Your balance is ${balance}.")
        else:
            print("Insufficient funds.")

    #exit
    elif act == "exit":
        break