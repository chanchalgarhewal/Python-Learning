a=int(input("enter first number:"))
b=int(input("enter second number:"))
operator=input("Enter a operator(+,-,*,/,%):")
if operator=="+":
    result=a+b
elif operator=="-":
    result=a-b
elif operator=="*":
    result=a*b
elif operator=="/":
    if b==0:
        result="can not br divide by zero"
    else:
        result=a/b
elif operator=="%":
    if b==0:
        result="can not be divide by zero"
    else: result=a%b

else:    
   result="Error:Invalid operator"
print("Result=",result)

    
     
   
