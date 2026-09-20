age=int(input("enter your age:"))
ticket_type=input("enter Ticket type (normal / premium)").lower()
if ticket_type=="normal":
    price=200
elif ticket_type=="premium":
    price=350
else:
    print("Invalid ticket Type")
    exit()

if age<5:
    discount=price
    final_price=0
elif age<=17:
    discount=price*0.50
    final_price=price-discount

elif age<=59:
    discount=0
    final_price=price
else:
    discount=price*0.30
    final_price=price-discount


print("ticket Price:",price)
print("Discount:",discount)
print("final Price:",final_price)
