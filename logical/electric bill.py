comsume=int(input("enter the unit consumed in kw:"))
if comsume<=50:
    print("cost of the electricity is:",cost)
elif comsume<=150:
    cost=50+(comsume-50)*2.50
    print("cost of the electricity is:",cost)
elif comsume<=250:
    cost=50+100+(comsume-150)*4
    print("cost of the electricity is:",cost)
else:
    cost=50+100+400+(comsume-250)*6
    print("cost of the electricity is:",cost)