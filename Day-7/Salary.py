Salary=int(input("Enter your Salary:"))
Experience=int(input("Enter you Experience:"))
if Experience >=10:
    bonus_percentage=20
    
elif Experience >=5:
     bonus_percentage=15
    
elif Experience >=2:
    bonus_percentage=10
    
else:
    bonus_percentage=5

Bonus=Salary*bonus_percentage/100
final_Salary=Salary+Bonus
print("\n Salary=",Salary)
print("bonus=",Bonus)
print("final_Salary=",final_Salary)
