name=input("Enter student name")
a=int(input("Enter marks  English:"))
b=int(input("Enter marks Maths:"))
c=int(input("Enter marks Python:"))
d=int(input("Enter marks AI:"))
e=int(input("Enter marks Databaase:"))

total_marks=a+b+c+d+e
Percentage=total_marks/5
print("Student Name:",name)
print("Total marks:",total_marks)
print("Percentage:",Percentage)

if Percentage>=90:
    print("Grade A")
elif Percentage>=80:
    print("Grade B")
elif Percentage>=70:
    print("Grade C")
elif Percentage>=60:
    print("Grade D")
elif Percentage>=50:
    print("Grade E")
else:
    print("Grade F")
