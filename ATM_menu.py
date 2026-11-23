balance = 50000
choice = ""

while choice != "3":
    print("\n===== ATM MANU =====")
    print("1. Check balance")
    print("2. Withdraw money")
    print("3. Exit")

    choice = input("Choose an option from (1-3): ")
    if choice == "1":
        print(f"Your balance is: ₦{balance}")

    elif choice == "2":
        withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

        if withdrawal_amount <= balance:
            balance -= withdrawal_amount
            print("Withdrawal successful.")
            print(f"Remaining balance: ₦{balance}")
        else:
            print("Insufficient funds.")

    elif choice == "3":
        print("Thank you for banking with us")
    else:
        print("Invalid option. Please try again.")