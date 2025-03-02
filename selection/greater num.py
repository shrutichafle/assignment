num1=int(input("enter a number:"))
num2=int(input("enter a number:"))
num3=int(input("enter a number:"))
if num1>num2 and num1>num3:
    print("the greater number is",num1)
elif num2>num1 and num2>num3:
    print("the greater number is",num2)
elif num3>num1 and num3>num2:
    print("the greater number is",num3)
else:
    print("write the different number")