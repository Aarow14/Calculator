

operater=input("enter a operator(+,-,*,/,or area :")

num1=float(input("enter the first number:"))
num2=float(input("enter the 2nd number:"))

if operater==("+"): result=num1+num2
elif operater==("-"):result=num1-num2
elif operater==("*"):result=num1*num2
elif operater==("/"):result=num1 / num2
elif operater==("area"):result=num1*num2
else:print(f"{operater} is not vaild")
print(round(result,3))

input("press enter to exit")

























