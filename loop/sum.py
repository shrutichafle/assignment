num=int(input("enter the number:"))
sum=0
for i in range(0,num+1):
    if i%2!=0:
        sum=sum+i
        print("the sum of odd number is:",sum)