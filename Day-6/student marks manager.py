name=input("Enter student name:")
a=int(input("Enter marks of subject 1:"))
b=int(input("Enter marks of subject 2:"))
c=int(input("Enter marks of subject 3:"))
total_marks=a+b+c
percentage=total_marks/3
print("Student Name:",name)
print("Total marks:",total_marks)
print("Percentage:",percentage)
if percentage>=90:
    print("Grade:A")
elif percentage>=80:
    print("Grade:B")
elif percentage>=70:
    print("Grade:C")
elif percentage>=60:
    print("Grade:D")
else:
    print("Grade:F")
