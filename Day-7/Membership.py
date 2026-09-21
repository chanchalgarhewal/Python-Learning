Amount=int(input("Enter a amount:"))
Membership=input("Are you a member?(yes/no):")

if Amount>=10000:
    discount=20
elif Amount>=5000:
    discount=15
elif Amount>=2000:
    discount=10
else:
    discount=0

if Amount>=10000 and Membership=="yes":
    discount=discount+5

discount_Amount=Amount*discount/100
Final_Amount=Amount-discount_Amount

print("Amount=",Amount)
print("discount_Amount=",discount_Amount)
print("Final_Amount=",Final_Amount)
