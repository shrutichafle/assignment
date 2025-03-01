principle=int(input("enter principle value:"))
rate=int(input("enter rate of interest:"))
time=int(input("enter time:"))
A=principle*(1+rate/100)**time
CI=A-principle
print("the final amount is:",CI)