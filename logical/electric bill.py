year=int(input("enter your experience in year:"))
if year>=5:
    bonus=10000
    print("your bonus is",bonus)
elif year>=3:
    bonus=5000
    print("your bonus is",bonus)
elif year>=1:
    bonus=2000
    print("your bonus is",bonus)
else:
    print("you have no bonus")