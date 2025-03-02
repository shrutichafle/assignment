number=int(input("enter a number:"))
if number>1:
    for i in range(2,number):
        if number%i==0:
            print("the number is not prime")
            break
    else:
        print(number,"is a prime number")
