balance=1000

print("1.Check Balance")
print("2.Deposit Money")
print("3.Withdraw Money")
print("4.Exit")

a=int(input("Enter your choice:"))

if a==1:
    print("Your Balance:",balance)

elif a==2:
    deposit=int(input("Enter deposit amount:"))
    balance = balance + deposite
    print("Amount Deposited Successfully")
    print("Your Balance :",balance)
elif a==3:
    withdraw=int(input("Enter deposit amount:"))

    if Withdraw <=balance:
        balance = balance - Withdraw
        print("Please collect your cash")
        print("Remaining Balance:",balance)
    else:
         print("Insuffivient Balance")
elif a==4:
    print("Thank you you for using ATM")
else:
    print("Invalid choice")
